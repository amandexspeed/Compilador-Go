import ply.yacc as yacc
import ply.lex as lex
from analiseLexica import tokens
from analiseLexica import lexer
from analiseLexica import breakLine
from analiseLexica import arquivos_go
import sintaxeAbstrata as sa
import logging

global isFine 
isFine = True

def p_programa(p):
    '''programa : pacote importacao declaracaoGlobal funcoes_codigo
                | pacote importacao funcoes_codigo'''
    if(len(p) == 5):
        p[0] = sa.ProgramaConcrete(p[1], p[2], p[3], p[4])
    else:
        p[0] = sa.ProgramaConcrete(p[1], p[2], None, p[3])

def p_empty(p):
    'empty :'
    pass

def p_pacote(p):
    '''pacote : PACKAGE ID delimitador 
              | PACKAGE ID NEWLINE'''
    p[0] = sa.PacoteConcrete(p[2])

def p_importacao(p):
    '''importacao : IMPORT STRING NEWLINE importacao
                  | IMPORT STRING delimitador importacao
                  | IMPORT STRING 
                  | empty'''
    
    if(len(p) == 5):
        if(p[4] == None):
            p[0] = sa.ImportacaoSimplesConcrete(p[2])
        else:
            p[0] = sa.ImportacaoCompostaConcrete(p[2], [p[4]])
    elif(len(p) == 3):
        p[0] = sa.ImportacaoSimplesConcrete(p[2])


def p_tipo(p):
    '''tipo : ID
            | STR
            | inteiro
            | float'''
    p[0] = p[1]

def p_inteiro(p):
    '''inteiro : INT
               | INT8 
               | INT16
               | INT32
               | INT64'''
    p[0] = p[1]

def p_float(p):
    '''float : FLOAT32
             | FLOAT64'''
    p[0] = p[1]

def p_tipo_nullavel(p):
    '''tipo_nullavel : tipo
                     | empty'''
    p[0] = p[1]

def p_declaracaoGlobal(p):
    '''declaracaoGlobal : declaracaoExplicitaGlobal
                        | declaracaoExplicitaGlobal NEWLINE
                        | declaracaoExplicitaGlobal NEWLINE declaracaoExplicitaGlobal'''
    p[0] = p[1]

def p_declaracaoExplicitaGlobal(p):
    '''declaracaoExplicitaGlobal : declaracaoExplicitaSimples
                                 | declaracaoExplicitaEmLista
                                 | declaracaoExplicitaEmListaEspacada'''
    p[0] = p[1]

def p_declaracaoExplicita(p):
    '''declaracaoExplicita : declaracaoExplicitaEmLista
                           | declaracaoExplicitaEmListaEspacada
                           | declaracaoExplicitaEmListaSimples'''
    p[0] = p[1]

def p_declaracaoExplicitaSimples(p):
    '''declaracaoExplicitaSimples : VAR tiposDeclaracoesExplicitas'''
    p[0] = p[2]

def p_tiposDeclaracoesExplicitas(p):
    '''tiposDeclaracoesExplicitas : declaracaoExplicitaSemValor
                                  | declaracaoExplicitaComValor'''  
    p[0] = p[1]

def p_declaracaoExplicitaSemValor(p):
    '''declaracaoExplicitaSemValor : ID tipo '''
    p[0] = sa.DeclaracaoExplicitaSimplesConcrete(p[1], p[2], None)

def p_declaracaoExplicitaComValor(p):
    '''declaracaoExplicitaComValor : ID tipo EQUALS constante'''
    p[0] = sa.DeclaracaoExplicitaSimplesConcrete(p[1],p[2], p[4])

def p_declaracaoExplicitaEmLista(p):
    '''declaracaoExplicitaEmLista : VAR BEG_PAREN listaExplicita END_PAREN'''
    p[0] = sa.DeclaracaoExplicitaCompostaConcrete(p[3])

def p_declaracaoExplicitaEmListaEspacada(p):
    '''declaracaoExplicitaEmListaEspacada : VAR BEG_PAREN NEWLINE listaExplicita END_PAREN'''
    p[0] = sa.DeclaracaoExplicitaCompostaConcrete(p[4])

def p_listaExplicita(p):
    '''listaExplicita : tiposDeclaracoesExplicitas
                      | listaExplicitaRecursiva
                      | tiposDeclaracoesExplicitas NEWLINE'''
    
    if(p[1].__class__ == list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_listaExplicitaRecursiva(p):
    '''listaExplicitaRecursiva : tiposDeclaracoesExplicitas NEWLINE listaExplicita'''
    p[0] = [p[1]] + p[3]

def p_declaracaoExplicitaEmListaSimples(p):
    '''declaracaoExplicitaEmListaSimples : VAR listaExplicitaSimples'''
    p[0] = p[1]

def p_listaExplicitaSimples(p):
    '''listaExplicitaSimples : lista_identificadores tipo
                             | lista_identificadores tipo COLON EQUALS lista_valores'''
    if(len(p) == 3):
        p[0] = [sa.DeclaracaoExplicitaSimplesConcrete(p[1], p[2], None)]
    else:
        p[0] = [sa.DeclaracaoExplicitaSimplesConcrete(p[2], p[2], p[5])]

def p_funcoes_codigo(p):
    '''funcoes_codigo : funcao delimitador funcoes_codigo
                      | funcao NEWLINE funcoes_codigo
                      | funcao
                      | empty'''
    p[0] = p[1]

def p_funcao(p):
    '''funcao : FUNC ID BEG_PAREN parametros END_PAREN tipo_nullavel BEG_BRACE codigo END_BRACE'''
    p[0] = sa.FuncaoConcrete(p[2], p[4], p[6], p[8]) 

def p_chamadaFuncao(p):
    '''chamadaFuncao : ID BEG_PAREN lista_valores END_PAREN
                     | ID BEG_PAREN END_PAREN'''
    if(len(p) == 5):
        p[0] = sa.ChamadaFuncaoConcrete(p[1], p[3])
    else:
        p[0] = sa.ChamadaFuncaoConcrete(p[1], None)

def p_parametros(p):
    '''parametros : parametro_simples
                  | parametros_tipo_unico
                  | parametros_varios_tipos
                  | empty'''
    p[0] = p[1]

def p_parametro_simples(p):
    '''parametro_simples : ID tipo'''
    p[0] = sa.ParametroSimplesConcrete(p[1], p[2])

def p_parametros_tipo_unico(p):
    '''parametros_tipo_unico : ID COMMA lista_parametros_tipo_unico'''
    p[0] = p[3].adicionarParametro(p[1])

def p_lista_parametros_tipo_unico(p):
    '''lista_parametros_tipo_unico : ID COMMA lista_parametros_tipo_unico 
                                   | ID tipo'''
    if(len(p) == 3):
        p[0] = sa.ParametroCompostoTipoUnicoConcrete([p[1]],p[2])
    else:
        if(p[3].__class__ == sa.ParametroCompostoTipoUnicoConcrete):
            p[3].adicionarParametro(p[1])
            p[0] = p[3]

def p_parametros_varios_tipos(p):
    '''parametros_varios_tipos : ID tipo COMMA lista_parametros_varios_tipos'''
    p[0] = p[4].adicionarParametro(sa.ParametroSimplesConcrete(p[1], p[2]))

def p_lista_parametros_varios_tipos(p):
    '''lista_parametros_varios_tipos : ID tipo COMMA lista_parametros_varios_tipos    
                                     | ID tipo'''
    if(len(p) == 3):
        p[0] = sa.ParametroCompostoVariosTiposConcrete([sa.ParametroSimplesConcrete(p[1], p[2])])
    else:
        if(p[4].__class__ == sa.ParametroCompostoVariosTiposConcrete):
            p[4].adicionarParametro(sa.ParametroSimplesConcrete(p[1], p[2]))
            p[0] = p[4]

def p_codigo(p):
    '''codigo : lista_estruturas'''
    p[0] = p[1]

def p_lista_estruturas(p):
    '''lista_estruturas : lista_estruturas estruturasBase
                        | empty'''
    if len(p) == 3:
        if(p[1].__class__ == sa.CodigoConcrete):
            p[1].adicionarEstrutura(p[2])
            p[0] = p[1]
        elif(p[2].__class__ != str):
            p[0] = sa.CodigoConcrete([p[2]])

def p_estruturasBase(p):
    '''estruturasBase : estruturas SEMICOLON
                      | estruturas NEWLINE
                      | NEWLINE'''
    p[0] = p[1]

def p_estruturas(p):
    """estruturas : atribuicao
                  | declaracao
                  | estrutura_if
                  | estrutura_for
                  | unario
                  | chamadaFuncao
                  | expressao_matematica_reduzida
                  | retorno"""
    p[0] = p[1]
 

def p_delimitador(p):
    '''delimitador  : SEMICOLON
                    | SEMICOLON NEWLINE'''
    p[0] = p[1]

def p_expressao(p):
    '''expressao : and
                 | or
                 | expressao_n2'''
    p[0] = p[1]

def p_and (p):
    '''and : expressao AMPERSAND AMPERSAND expressao_n2'''
    p[0] = sa.ExpressaoAND (p[1], p[4])

def p_or (p):
    '''or : expressao PIPE PIPE expressao_n2'''
    p[0] =  sa.ExpressaoOR (p[1], p[4])

def p_expressao_n2(p):
    '''expressao_n2 : equals
                    | different
                    | greater
                    | less
                    | greater_or_equal
                    | less_or_equal
                    | expressao_n3'''
    p[0] = p[1]

def p_equals (p):
    '''equals : expressao_n2 EQUALITY expressao_n3'''
    p[0] = sa.ExpressoaIGUAL (p[1], p[3])

def p_different (p):
    '''different : expressao_n3 DIFFERENT expressao_n3'''
    p[0] = sa.ExpressaoDIFFERENT (p[1], p[4])

def p_greater (p):
    '''greater : expressao_n2 GREATER expressao_n3'''
    p[0] = sa.ExpressaoGREATER(p[1], p[3])

def p_less (p):
    '''less : expressao_n2 LESS expressao_n3'''
    p[0] = sa.ExpressaoLESS (p[1], p[3])

def p_greater_or_equal (p):
    '''greater_or_equal : expressao_n2 GREATER EQUALS expressao_n3'''
    p[0] = sa.ExpressaoGREAT_OR_EQUAL (p[1], p[4])

def p_less_or_equal (p):
    '''less_or_equal : expressao_n2 LESS EQUALS expressao_n3'''
    p[0] = sa.ExpressaoLESS_OR_EQUAL(p[1], p[4])
    
def p_expressao_n3(p):

    '''expressao_n3 : soma 
                    | sub 
                    | expressao_n4 '''
    p[0] = p[1]


def p_soma(p):
    '''soma : expressao_n3 PLUS expressao_n4'''
    p[0] = sa.ExpressaoSOMA (p[1] , p[3])

def p_sub(p):
    '''sub : expressao_n3 MINUS expressao_n4'''
    p[0] = sa.ExpressaoSUB(p[1] , p[3])

def p_expressao_n4(p):
    ''' expressao_n4 : mult 
                     | div 
                     | mod 
                     | expressao_n5 '''
    p[0] = p[1]

def p_mult(p):
    '''mult : expressao_n4 TIMES expressao_n5'''
    p[0] = sa.ExpressaoMULT (p[1] , p[3])

def p_mod(p):
    '''mod : expressao_n4 MOD expressao_n5'''
    p[0] = sa.ExpressaoMOD (p[1], p[3])

def p_div(p):
    '''div : expressao_n4 DIVISION expressao_n5'''
    p[0] = sa.ExpressaoDIV (p[1], p[3])

def p_expressao_n5(p):
    '''expressao_n5 : unario
                    | operando
                    | negation'''
    p[0] = p[1]

def p_negation (p):
    '''negation : EXCLAMATION operando'''
    p[0] = sa.ExpressaoNEGATION (p[2])

def p_unario(p):
    ''' unario : incremento
               | decremento
               | pre_incremento
               | pre_decremento'''
    p[0] = p[1]

def p_incremento(p):
    '''incremento : ID INCREMENT'''
    p[0] = sa.ExpressaoINCREMENTO (p[1])

def p_pre_incremento(p):
    '''pre_incremento : INCREMENT ID'''
    p[0] = sa.ExpressaoPRE_INCREMENTO (p[1])

def p_decremento(p):
    '''decremento : ID DECREMENT'''
    p[0] = sa.ExpressaoDECREMENTO (p[1])

def p_pre_decremento(p):
    '''pre_decremento : DECREMENT ID''' 
    p[0] = sa.ExpressaoPRE_DECREMENTO (p[1])

def p_operando(p):
    '''operando : constante
                | chamadaFuncao
                | expParenteses'''
    p[0] = p[1]

def p_constante(p):
    '''constante : constante_numero
                 | constante_string
                 | constante_booleano
                 | constante_id'''
    p[0] = p[1]

def p_constante_numero(p):
    '''constante_numero : NUMBER'''
    p[0] = sa.ConstanteConcreto (p[1],'Number')

def p_constante_string(p):
    '''constante_string : STRING'''
    p[0] = sa.ConstanteConcreto (p[1], 'String')

def p_constante_booleano(p):
    '''constante_booleano : TRUE
                          | FALSE'''
    p[0] = sa.ConstanteConcreto (p[1], 'Boolean')

def p_constante_id(p):
    '''constante_id : ID'''
    p[0] = sa.ConstanteConcreto (p[1], 'ID')

def p_expParenteses(p):
    '''expParenteses : BEG_PAREN expressao END_PAREN'''
    p[0] = sa.ExpressaoPARENTESE (p[2])

def p_estrutura_for(p):
    '''estrutura_for : for_CLIKE
                     | for_infinito
                     | for_while'''
    p[0] = p[1]

def p_for_CLIKE(p): 
    '''for_CLIKE : FOR declaracao_for SEMICOLON expressao SEMICOLON expressao BEG_BRACE codigo END_BRACE
                 | FOR atribuicao_for SEMICOLON expressao SEMICOLON expressao BEG_BRACE codigo END_BRACE'''
    p[0] = sa.For_CLIKEconcrete(p[2],p[4],p[6],p[8])

def p_atribuicao_for(p):
    '''atribuicao_for : ID EQUALS expressao'''
    p[0] = sa.AtribuicaoConcrete([p[1]], [p[3]])

def p_declaracao_for(p):
    '''declaracao_for : ID COLON EQUALS expressao'''
    p[0] = sa.DeclaracaoCurtaConcrete([p[1]], [p[4]])

def p_for_infinito(p):
    '''for_infinito : FOR BEG_BRACE codigo END_BRACE'''
    p[0] = sa.For_INFINITOconcrete(p[3])

def p_for_while(p):
    '''for_while : FOR expressao BEG_BRACE codigo END_BRACE'''
    p[0] = sa.For_WHILEconcrete(p[2],p[4])


def p_estrutura_if(p):
    '''estrutura_if : IF expressao BEG_BRACE codigo END_BRACE estrutura_else
                    | IF expressao BEG_BRACE codigo END_BRACE'''
    if(len(p) == 7):
        p[0] = sa.EstruturaIF_ELSEconcrete(p[2], p[4], p[6])
    else:
        p[0] = sa.EstruturaIFconcrete(p[2], p[4])

def p_estrutura_else(p):
    '''estrutura_else : ELSE BEG_BRACE codigo END_BRACE
                      | ELSE estrutura_if'''
    if(len(p) == 5):
        p[0] = sa.EstruturaELSEconcrete(p[3])
    elif(len(p) == 3):
        p[0] = sa.EstruturaELSE_IFconcrete(p[2])

def p_retorno(p):
    '''retorno : RETURN expressao'''
    p[0] = sa.RetornoFuncaoConcrete(p[2])

def p_atribuicao(p):
    '''atribuicao : lista_identificadores EQUALS lista_valores'''
    p[0] = sa.AtribuicaoConcrete(p[1], p[3])
    
def p_declaracao(p):
    '''declaracao : declaracaoCurta
                  | declaracaoExplicita'''
    p[0] = p[1]

def p_declaracaoCurta(p):
    '''declaracaoCurta : lista_identificadores COLON EQUALS lista_valores'''
    p[0] = sa.DeclaracaoCurtaConcrete(p[1], p[4])

def p_lista_identificadores(p):
    '''lista_identificadores : lista_identificadores COMMA ID
                             | ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_lista_valores(p):
   '''lista_valores : lista_valores COMMA expressao
                    | expressao'''
   if len(p) == 2:
        p[0] = [p[1]]
   else:
        p[0] = p[1] + [p[3]]

def p_expressao_matematica_reduzida(p):
    '''expressao_matematica_reduzida : assign_plus
                                     | assign_minus
                                     | assign_mult
                                     | assign_div'''
    p[0] = p[1]

def p_assign_plus(p):
    '''assign_plus : ID PLUS EQUALS expressao'''
    p[0] = sa.assignPlus(p[1], p[4])

def p_assign_minus(p):
    '''assign_minus : ID MINUS EQUALS expressao'''
    p[0] = sa.assignMinus(p[1], p[4])

def p_assign_mult(p):
    '''assign_mult : ID TIMES EQUALS expressao'''
    p[0] = sa.assignMult(p[1], p[4])

def p_assign_div(p):
    '''assign_div : ID DIVISION EQUALS expressao'''
    p[0] = sa.assignDiv(p[1], p[4])

def p_error(p):
    print("Erro sintático na entrada!")
    global isFine 
    isFine = False

def main():
    global isFine

    with open("logSintatico.txt", "w") as log:
        for arquivo in arquivos_go:
            
            isFine = True
            print("-----------Analise Sintática do arquivo: ", arquivo,"-----------")
            print("\n")
            log.write(f"-----------Analise Sintática do arquivo: {arquivo} -----------\n")
            
            f = open(arquivo, "r")

            lexer.input(f.read())
            parser = yacc.yacc(start='programa')
            result = parser.parse(debug=1)
            print(result)
            log.write(str(result))
            log.write("\n")
            if(isFine):
                print("Analise sintatica realizada com sucesso!")
                log.write("Analise sintatica realizada com sucesso!")
            else:
                print("Analise sintatica constatou erro!")
                log.write("Analise sintatica constatou erro!")

            print("\n\n")
            log.write("\n\n")

if __name__ == "__main__":
    main()
