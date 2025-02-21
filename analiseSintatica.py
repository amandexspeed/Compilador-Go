import ply.yacc as yacc
import ply.lex as lex
from analiseLexica import tokens
from analiseLexica import lexer
from analiseLexica import breakLine
from analiseLexica import arquivos_go
import sintaxeAbstrata as sa

variaveis = {}

def p_programa(p):
    '''programa : pacote importacao declaracaoGlobal funcoes_codigo'''
    p[0] = sa.ProgramaConcrete(p[1], p[2], p[3], p[4])

def p_empty(p):
    'empty :'
    pass

def p_pacote(p):
    '''pacote : PACKAGE ID NEWLINE '''
    p[0] = sa.PacoteConcrete(p[2])

def p_importacao(p):
    '''importacao : IMPORT ID NEWLINE importacao
                  | empty'''
    
    if(len(p) == 5):
        if(p[4] == None):
            p[0] = sa.ImportacaoSimplesConcrete(p[2])
        else:
            p[0] = sa.ImportacaoCompostaConcrete(p[2], p[4])
    else:
        p[0] = p[1]

def p_declaracaoGlobal(p):
    '''declaracaoGlobal : regrasDeclaracaoGlobal
                        | regrasDeclaracaoGlobal NEWLINE
                        | empty'''
    p[0] = p[1]

def p_regrasDeclaracaoGlobal(p):
    '''regrasDeclaracaoGlobal : declaracaoGlobalSimples
                              | declaracaoEmLista
                              | declaracaoEmListaEspacada'''
    p[0] = p[1]

def p_declaracaoGlobalSimples(p):
    '''declaracaoGlobalSimples : VAR tiposDeclaracoesGlobais'''
    p[0] = p[2]

def p_tiposDeclaracoesGlobais(p):
    '''tiposDeclaracoesGlobais : declaracaoGlobalSemValor
                               | declaracaoGlobalComValor'''  
    p[0] = p[1]

def p_declaracaoGlobalSemValor(p):
    '''declaracaoGlobalSemValor : ID ID'''
    p[0] = sa.DeclaracaoGlobalSimplesConcrete(p[1], p[2])

def p_declaracaoGlobalComValor(p):
    '''declaracaoGlobalComValor : ID ID EQUALS constante'''
    p[0] = sa.DeclaracaoGlobalSimplesComValorConcrete(p[1],p[2], p[4])

def p_declaracaoEmLista(p):
    '''declaracaoEmLista : VAR BEG_PAREN listaGlobal END_PAREN'''
    p[0] = sa.DeclaracaoGlobalCompostaConcrete(p[3])

def p_declaracaoEmListaEspacada(p):
    '''declaracaoEmListaEspacada : VAR BEG_PAREN NEWLINE listaGlobal END_PAREN'''
    p[0] = sa.DeclaracaoGlobalCompostaConcrete(p[4])

def p_listaGlobal(p):
    '''listaGlobal : tiposDeclaracoesGlobais
                   | listaGlobalRecursiva
                   | tiposDeclaracoesGlobais NEWLINE'''
    if(p[1].__class__ == list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_listaGlobalRecursiva(p):
    '''listaGlobalRecursiva : tiposDeclaracoesGlobais NEWLINE listaGlobal'''
    p[0] = [p[1]] + p[3]

def p_funcoes_codigo(p):
    '''funcoes_codigo : funcao delimitador funcoes_codigo
                      | funcao
                      | empty'''
    p[0] = p[1]

def p_funcao(p):
    '''funcao : FUNC ID BEG_PAREN lista_parametros END_PAREN tipo_retorno BEG_BRACE codigo END_BRACE'''
    p[0] = sa.FuncaoConcrete(p[2], p[4], p[6], p[8]) 

def p_tipo_retorno(p):
    '''tipo_retorno : ID
                    | empty'''
    p[0] = p[1]

def p_codigo(p):
    '''codigo : lista_estruturas'''
    p[0] = p[1]

def p_lista_estruturas(p):
    '''lista_estruturas : lista_estruturas estruturasBase
                        | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        if(p[1].__class__ == list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]

def p_estruturasBase(p):
    '''estruturasBase : estruturas delimitador
                      | NEWLINE'''
                      
    p[0] = p[1]

def p_estruturas(p):
    """estruturas : atribuicao
                  | declaracao
                  | estrutura_if
                  | estrutura_for
                  | unario
                  | chamadaFuncao"""
    p[0] = p[1]
 

def p_delimitador(p):
    '''delimitador : NEWLINE
                   | SEMICOLON'''
    p[0] = p[1]

def p_expressao(p):
    '''expressao : and
                 | or
                 | expressao_n2'''
    p[0] = p[1]

def p_and (p):
    '''and : expressao AMPERSAND AMPERSAND expressao_n2'''
    p[0] = p[1] and p[4]

def p_or (p):
    '''or : expressao PIPE PIPE expressao_n2'''
    p[0] = p[1] or p[4]

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
    '''equals : expressao_n2 EQUALS EQUALS expressao_n3'''
    p[0] = p[1] == p[4]

def p_different (p):
    '''different : expressao_n3 DIFFERENT expressao_n3'''
    p[0] = p[1] != p[4]

def p_greater (p):
    '''greater : expressao_n2 GREATER expressao_n3'''
    p[0] = p[1] > p[3]

def p_less (p):
    '''less : expressao_n2 LESS expressao_n3'''
    p[0] = p[1] < p[3]

def p_greater_or_equal (p):
    '''greater_or_equal : expressao_n2 GREATER EQUALS expressao_n3'''
    p[0] = p[1] >= p[4]

def p_less_or_equal (p):
    '''less_or_equal : expressao_n2 LESS EQUALS expressao_n3'''
    p[0] = p[1] <= p[4]
    
def p_expressao_n3(p):

    ''' expressao_n3 : soma 
                     | sub 
                     | expressao_n4 '''
    p[0] = p[1]


def p_soma(p):
    '''soma : expressao_n3 PLUS expressao_n4'''
    p[0] = p[1] + p[3]

def p_sub(p):
    '''sub : expressao_n3 MINUS expressao_n4'''
    p[0] = p[1] - p[3]

def p_expressao_n4(p):

    ''' expressao_n4 : mult 
                     | div 
                     | mod 
                     | expressao_n5 '''
    p[0] = p[1]


def p_mult(p):
    '''mult : expressao_n4 TIMES expressao_n5'''
    p[0] = p[1] * p[3]

def p_mod(p):
    '''mod : expressao_n4 MOD expressao_n5'''
    p[0] = p[1] % p[3]

def p_div(p):
    '''div : expressao_n4 DIVISION expressao_n5'''
    p[0] = p[1] / p[3]

def p_expressao_n5(p):
    '''expressao_n5 : unario
                    | operando
                    | negation'''
    p[0] = p[1]

def p_unario(p):
    ''' unario : incremento
               | decremento
               | pre_incremento
               | pre_decremento'''
    p[0] = p[1]

def p_negation (p):
    '''negation : EXCLAMATION operando'''
    p[0] = not p[2]

def p_incremento(p):
    '''incremento : ID INCREMENT'''
    p[0] = variaveis[p[1]] + 1

def p_pre_incremento(p):
    '''pre_incremento : INCREMENT ID'''
    p[0] = variaveis[p[1]] + 1

def p_decremento(p):
    '''decremento : ID DECREMENT'''
    p[0] = variaveis[p[1]] - 1

def p_pre_decremento(p):
    '''pre_decremento : DECREMENT ID''' 
    p[0] = variaveis[p[1]] - 1

def p_operando(p):
    '''operando : identificador
                | constante
                | chamadaFuncao
                | expParenteses'''
    p[0] = p[1]

def p_constante(p):
    '''constante : NUMBER
                 | STRING
                 | TRUE
                 | FALSE'''
    p[0] = p[1]

def p_identificador(p):
    '''identificador : ID'''
    if(variaveis.get(p[1]) == None):
        p[0]=p[1]
    else:
        p[0] = variaveis[p[1]]

def p_expParenteses(p):
    '''expParenteses : BEG_PAREN expressao END_PAREN'''
    p[0] = p[2]

def p_estrutura_for(p):
    '''estrutura_for : for_CLIKE
                     | for_infinito
                     | for_while'''
    p[0] = p[1]

def p_for_CLIKE(p): 
    '''for_CLIKE : FOR declaracao SEMICOLON expressao SEMICOLON expressao BEG_BRACE codigo END_BRACE'''
    p[0] = (p[2],p[4],p[6],p[8])

def p_for_infinito(p):
    '''for_infinito : FOR BEG_BRACE codigo END_BRACE'''
    p[0] = p[3]

def p_for_while(p):
    '''for_while : FOR expressao BEG_BRACE codigo END_BRACE'''
    p[0] = (p[2],p[4])


def p_estrutura_if(p):
    '''estrutura_if : IF expressao BEG_BRACE codigo END_BRACE estrutura_else
                    | IF expressao BEG_BRACE codigo END_BRACE'''
    if(p[2]):
        p[0] = p[4]
    else:
        if(len(p) == 6):
            p[0] = p[6]
        else:
            p[0] = []

def p_estrutura_else(p):
    '''estrutura_else : ELSE BEG_BRACE codigo END_BRACE
                      | ELSE estrutura_if'''
    if(len(p) == 2):
        p[0] = []
    elif(p[4] == None):
        p[0] = p[2]
    else:
        p[0] = p[3]


def p_atribuicao(p):
    '''atribuicao : lista_identificadores EQUALS lista_valores
                  | expressao_matematica_reduzida'''
    
    for i in range(len(p[1])):
        variaveis[p[1][i]] = p[3][i]
    p[0] = p[3]

def p_expressao_matematica_reduzida(p):
    '''expressao_matematica_reduzida : assign_plus
                                     | assign_minus
                                     | assign_mult
                                     | assign_div'''
    p[0] = p[1]

def p_assign_plus(p):
    '''assign_plus : ID PLUS EQUALS expressao'''
    p[0] = variaveis[p[1]] + p[4]

def p_assign_minus(p):
    '''assign_minus : ID MINUS EQUALS expressao'''
    p[0] = variaveis[p[1]] - p[4]

def p_assign_mult(p):
    '''assign_mult : ID TIMES EQUALS expressao'''
    p[0] = variaveis[p[1]] * p[4]

def p_assign_div(p):
    '''assign_div : ID DIVISION EQUALS expressao'''
    p[0] = variaveis[p[1]] / p[4]
    
def p_declaracao(p):
    '''declaracao : lista_identificadores COLON EQUALS lista_valores'''
    
    for i in range(len(p[1])):
        variaveis[p[1][i]] = p[4][i]
    p[0] = p[4]

def p_chamadaFuncao(p):
    '''chamadaFuncao : ID BEG_PAREN lista_parametros END_PAREN'''
    p[0] = (p[1], p[3])

def p_lista_parametros(p):
    '''lista_parametros : lista_identificadores
                        | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

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

def main():

    for arquivo in arquivos_go:
        print("-----------Analise Sintática do arquivo: ", arquivo,"-----------")
        f = open(arquivo, "r")

        lexer.input(f.read())
        parser = yacc.yacc(start='programa')
        result = parser.parse(debug=1)
        print(result)

if __name__ == "__main__":
    main()
