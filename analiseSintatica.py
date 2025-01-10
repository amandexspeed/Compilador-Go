import ply.yacc as yacc
import ply.lex as lex
from analiseLexica import tokens
from analiseLexica import lexer
from analiseLexica import breakLine
from analiseLexica import arquivos_go

variaveis = {}

def p_programa(p):
    '''programa : pacote importacao funcoes_codigo'''
    p[0] = (p[1], p[2], p[3])

def p_funcoes_codigo(p):
    '''funcoes_codigo : funcao funcoes_codigo
                      | codigo funcoes_codigo
                      | empty'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_pacote(p):
    '''pacote : PACKAGE ID'''
    p[0] = p[1]

def p_importacao(p):
    '''importacao : IMPORT ID importacao
                  | empty'''
    p[0] = p[1]

def p_funcao(p):
    '''funcao : FUNC ID BEG_PAREN lista_parametros END_PAREN tipo_retorno BEG_BRACE codigo END_BRACE'''
    p[0] = p[7]
    
'''p[0] = (p[2], p[4], p[6], p[8])''' 

def p_tipo_retorno(p):
    '''tipo_retorno : ID
                    | empty'''
    p[0] = p[1]

def p_codigo(p):
    '''codigo : expressao_matematica_reduzida codigo
              | atribuicao codigo
              | declaracao codigo
              | estrutura_if codigo
              | estrutura_for codigo
              | empty'''
    if len(p) == 2:
        p[0] = []
    else:
        if(p[1].__class__ == list):
            p[0] = p[1] + [p[2]]
        else:
            if(p[2].__class__ == list and p[2] != None):
                p[0] = [p[1]] + p[2]
            else:
                p[0] = p[1]

def p_codigo_reduzido(p):
    '''codigo_reduzido : expressao_matematica_reduzida
                       | atribuicao
                       | declaracao
                       | estrutura_if
                       | estrutura_for'''
    p[0] = p[1]

def p_expressao(p):
    '''expressao : expressao_matematica
                 | expressao_logica'''
    p[0] = p[1]
    
def p_expressao_matematica(p):

    ''' expressao_matematica : soma 
                             | sub 
                             | p_expMatMaiorPresc '''
    p[0] = p[1]

def p_soma(p):
    '''soma : expressao_matematica PLUS p_expMatMaiorPresc'''
    p[0] = p[1] + p[3]

def p_sub(p):
    '''sub : expressao_matematica MINUS p_expMatMaiorPresc'''
    p[0] = p[1] - p[3]

def p_expMatMaiorPresc(p):
    '''p_expMatMaiorPresc : mult 
                          | div
                          | mod 
                          | operando''' 
    p[0] = p[1]

def p_mult(p):
    '''mult : p_expMatMaiorPresc TIMES operando'''
    p[0] = p[1] * p[3]

def p_mod(p):
    '''mod : p_expMatMaiorPresc MOD operando'''
    p[0] = p[1] % p[3]

def p_div(p):
    '''div : p_expMatMaiorPresc DIVISION operando'''
    p[0] = p[1] / p[3]

def p_incremento(p):
    '''incremento : ID PLUS PLUS
                  | ID PLUS PLUS SEMICOLON'''
    p[0] = variaveis[p[1]] + 1

def p_pre_incremento(p):
    '''pre_incremento : PLUS PLUS ID 
                  | PLUS PLUS ID SEMICOLON'''
    p[0] = variaveis[p[1]] + 1

def p_decremento(p):
    '''decremento : ID MINUS MINUS
                  | ID MINUS MINUS SEMICOLON'''
    p[0] = variaveis[p[1]] - 1

def p_pre_decremento(p):
    '''pre_decremento : MINUS MINUS ID
                  | MINUS MINUS ID SEMICOLON'''
    p[0] = variaveis[p[1]] - 1

def p_assign_plus(p):
    '''assign_plus : ID PLUS EQUALS NUMBER'''
    p[0] = variaveis[p[1]] + p[4]

def p_assign_minus(p):
    '''assign_minus : ID MINUS EQUALS NUMBER'''
    p[0] = variaveis[p[1]] - p[4]

def p_assign_mult(p):
    '''assign_mult : ID TIMES EQUALS NUMBER'''
    p[0] = variaveis[p[1]] * p[4]

def p_assign_div(p):
    '''assign_div : ID DIVISION EQUALS NUMBER'''
    p[0] = variaveis[p[1]] / p[4]

def p_expressao_matematica_reduzida(p):
    '''expressao_matematica_reduzida : assign_plus
                                     | assign_minus
                                     | assign_mult
                                     | assign_div
                                     | incremento
                                     | pre_incremento
                                     | decremento
                                     | pre_decremento'''
    p[0] = p[1]

def p_operando(p):
    '''operando : identificador
                | NUMBER 
                | STRING 
                | expParenteses'''
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
    
def p_expressao_logica(p):
    '''expressao_logica : and
                        | or
                        | equals
                        | different
                        | greater
                        | less
                        | greater_or_equal
                        | less_or_equal
                        | negation
                        | TRUE
                        | FALSE'''
    p[0] = p[1]

def p_and (p):
    '''and : expressao AMPERSAND AMPERSAND expressao'''
    p[0] = p[1] and p[4]

def p_or (p):
    '''or : expressao PIPE PIPE expressao'''
    p[0] = p[1] or p[4]

def p_equals (p):
    '''equals : expressao EQUALS EQUALS expressao'''
    p[0] = p[1] == p[4]

def p_different (p):
    '''different : expressao EXCLAMATION EQUALS expressao'''
    p[0] = p[1] != p[4]

def p_greater (p):
    '''greater : expressao GREATER expressao'''
    p[0] = p[1] > p[3]

def p_less (p):
    '''less : expressao LESS expressao'''
    p[0] = p[1] < p[3]

def p_greater_or_equal (p):
    '''greater_or_equal : expressao GREATER EQUALS expressao'''
    p[0] = p[1] >= p[4]

def p_less_or_equal (p):
    '''less_or_equal : expressao LESS EQUALS expressao'''
    p[0] = p[1] <= p[4]

def p_negation (p):
    '''negation : EXCLAMATION expressao'''
    p[0] = not p[2]

def p_estrutura_for(p):
    '''estrutura_for : for_CLIKE
                     | for_infinito
                     | for_while'''
    p[0] = p[1]

def p_for_CLIKE(p): 
    '''for_CLIKE : FOR declaracao SEMICOLON expressao SEMICOLON expressao_matematica BEG_BRACE codigo END_BRACE'''
    p[0] = (p[2],p[4],p[6],p[8])

def p_for_infinito(p):
    '''for_infinito : FOR BEG_BRACE codigo END_BRACE'''
    p[0] = p[3]

def p_for_while(p):
    '''for_while : FOR expressao BEG_BRACE codigo END_BRACE'''
    p[0] = (p[2],p[4])

def p_estrutura_if(p):
    '''estrutura_if : IF expressao BEG_BRACE codigo END_BRACE estrutura_else'''
    if(p[2]):
        p[0] = p[4]
    else:
        p[0] = p[6]

def p_estrutura_else(p):
    '''estrutura_else : ELSE BEG_BRACE codigo END_BRACE
                      | ELSE estrutura_if
                      | empty'''
    if(len(p) == 2):
        p[0] = []
    elif(p[4] == None):
        p[0] = p[2]
    else:
        p[0] = p[3]
        
def p_atribuicao(p):
    '''atribuicao : lista_identificadores EQUALS lista_valores
                  | lista_identificadores EQUALS lista_valores SEMICOLON'''
    
    for i in range(len(p[1])):
        variaveis[p[1][i]] = p[3][i]
    p[0] = p[3]
    
def p_declaracao(p):
    '''declaracao : lista_identificadores COLON EQUALS lista_valores
                  | lista_identificadores COLON EQUALS lista_valores SEMICOLON'''
    
    for i in range(len(p[1])):
        variaveis[p[1][i]] = p[4][i]
    p[0] = p[4]

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