import ply.yacc as yacc
import ply.lex as lex
from analiseLexica import tokens
from analiseLexica import lexer

def p_exp_exp(p):

    ''' exp : soma 
        | sub 
        | exp1 '''
    p[0] = p[1]

def p_exp_soma(p):
    '''soma : exp PLUS exp1'''
    p[0] = p[1] + p[3]

def p_exp_sub(p):
    '''sub : exp MINUS exp1'''
    p[0] = p[1] - p[3]

def p_exp1(p):
    '''exp1 : mult 
       | div 
       | exp2''' 
    p[0] = p[1]

def p_exp_mult(p):
    '''mult : exp1 TIMES exp2'''
    p[0] = p[1] * p[3]

def p_exp_div(p):
    '''div : exp1 DIVISION exp2'''
    p[0] = p[1] / p[3]

def p_exp_exp2(p):
    '''exp2 : ID
        | NUMBER 
        | STRING 
        | exp3 '''
    p[0] = p[1]

def p_exp_exp3(p):
    '''exp3 : BEG_PAREN exp END_PAREN'''
    p[0] = p[2]

lexer.input("2*(4+2)")
parser = yacc.yacc()
result = parser.parse(debug=False)
print(result)