import ply.yacc as yacc
import ply.lex as lex
from analiseLexica import tokens
from analiseLexica import lexer
from analiseLexica import arquivos_go

def p_expressao(p):
    '''expressao : expressao_matematica
                 | expressao_logica
                 | operando'''
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

def p_assign_plus(p):
    '''assign_plus : ID PLUS EQUALS NUMBER'''
    p[0] = p[1] + p[4]

def p_assign_minus(p):
    '''assign_minus : ID MINUS EQUALS NUMBER'''
    p[0] = p[1] - p[4]

def p_assign_mult(p):
    '''assign_mult : ID TIMES EQUALS NUMBER'''
    p[0] = p[1] * p[4]

def p_assign_div(p):
    '''assign_div : ID DIVISION EQUALS NUMBER'''
    p[0] = p[1] / p[4]

def p_expressao_matematica_reduzida(p):
    '''expressao_matematica_reduzida : assign_plus
                                     | assign_minus
                                     | assign_mult
                                     | assign_div'''
    p[0] = p[1]

def p_operando(p):
    '''operando : ID
                | NUMBER 
                | STRING 
                | expParenteses'''
    p[0] = p[1]

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
                        | true
                        | false'''
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
    '''for_CLIKE : for declaracao SEMICOLON expressao SEMICOLON expressao_matematica BEG_BRACE codigo END_BRACE'''
    variaveis = p[2]
    while (p[4]):
        p[0] = p[8]
        for i in range(len(variaveis)):
            variaveis[i] = p[6]

def p_for_infinito(p):
    '''for_infinito : for BEG_BRACE codigo END_BRACE'''
    while True:
        p[0] = p[3]

def p_for_while(p):
    '''for_while : for expressao BEG_BRACE codigo END_BRACE'''
    while p[2]:
        p[0] = p[4]

def p_atribuicao(p):
    '''atribuicao : lista_identificadores EQUALS lista_valores'''
    p[0] = p[3]

def p_declaracao(p):
    '''declaracao : lista_identificadores COLON EQUALS lista_valores'''
    p[0] = p[4]

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

def p_empty(p):
    'empty :'
    pass

def p_codigo(p):
    '''codigo : codigo expressao_matematica_reduzida
              | codigo atribuicao
              | codigo declaracao
              | codigo estrutura_for
              | empty'''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]



def main():

    for arquivo in arquivos_go:
        print("-----------Analise Sintática do arquivo: ", arquivo,"-----------")
        f = open(arquivo, "r")

        lexer.input(f.read())
        parser = yacc.yacc()
        result = parser.parse(debug=False)
        print(result)

if __name__ == "__main__":
    main()