import os

# Listar todos os arquivos no diretório
arquivos = os.listdir(os.getcwd())

# Filtrar arquivos pelo tipo
arquivos_go = [arquivo for arquivo in arquivos if arquivo.endswith('.go')]

import ply.lex as lex     #importa módulo ply.lex e o renomeia para lex

#Tipos numéricos
numberTypes = {
             }

#Lista com as palavras reservadas
reserved = {
    'true':'TRUE',
    'false':'FALSE',
    'break':'BREAK',
    'const':'CONST',
    'else':'ELSE',
    'for':'FOR',
    'func':'FUNC',
    'if':'IF',
    'import':'IMPORT',
    'package':'PACKAGE',
    'return':'RETURN', 
    'var':'VAR',

    'int':'INT', 
    'int8':'INT8', 
    'int16':'INT16', 
    'int32':'INT32', 
    'int64':'INT64', 
    'float32':'FLOAT32', 
    'float64':'FLOAT64'  
}

breakLine = {1: 0}
# Definindo Tokens e padroes
tokens = ["STR","INCREMENT","PLUS","DECREMENT","MINUS","TIMES","DIVISION","MOD","POWER","DIFFERENT","EQUALS","LESS","GREATER","BEG_PAREN","END_PAREN","BEG_BRACE","END_BRACE","NUMBER","QUOTATION_MARKS","EXCLAMATION","COLON","SEMICOLON","COMMA","ID","STRING","NEWLINE","AMPERSAND","PIPE"] + list(reserved.values())

def t_COMMENT(t):
    r'(//.*)'
    adjustLineComment(t)
    pass

def adjustLineComment(t):
    global breakLine
    breakLine[t.lineno] = t.lexpos + 1
    t.lexer.lineno += len(t.value)

def t_MULTILINE_COMMENT(t):
    r'(/\*(.|\n)*?\*/)'
    adjustBlockComment(t)
    pass

def adjustBlockComment(t):
    global breakLine
    textParts = t.value.split("\n")
    for text in textParts:
        breakLine[t.lineno] = t.lexpos + 1
        t.lexer.lineno += 1
    t.lexer.lineno -= 1
t_STR= r'string'
t_PLUS    = r'\+'
t_INCREMENT = r'\+\+'
t_MINUS   = r'-'
t_DECREMENT = r'--'
t_EQUALS  = r'='
t_DIFFERENT = r'!='
t_TIMES   = r'\*'
t_DIVISION = r'/'
t_MOD = r'%'
t_POWER   = r'\^'
t_LESS = r'<'
t_GREATER = r'>'
t_BEG_PAREN = r'\('
t_END_PAREN = r'\)'
t_BEG_BRACE = r'\{'
t_END_BRACE = r'\}'
t_QUOTATION_MARKS = r'\"'
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_EXCLAMATION = r'\!'
t_AMPERSAND = r'\&'
t_PIPE = r'\|'

t_ignore = ' \t.'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_STRING(t):
    r'\".*?\"'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_error(t):
    print("Illegal character -", t.value[0],"- Line: ", t.lineno," Column: ",t.lexpos)
    t.lexer.skip(1)
    global isFine 
    isFine  = False

def t_NEWLINE(t):
    r'\n+'
    global breakLine
    for i in range(t.value.count("\n")):
        breakLine[(t.lineno + i)+1] = t.lexpos + i
    t.lexer.lineno += len(t.value)
    return t

lexer = lex.lex()

def main():

    global isFine
    global lexer
    global breakLine

    # Criando Analisador Lexico, passando entrada
    if len(arquivos_go) == 0:
        print("Nenhum arquivo .go encontrado!")

    else:   
         
        isFine = True
        
        for arquivo in arquivos_go:
            print("-----------Analise lexica do arquivo: ", arquivo,"-----------")
            breakLine = {1: 0}
            f = open(arquivo, "r")
            
            lexer = lex.lex()
            lexer.input(f.read())

            # Realizando analise lexica
            for tok in lexer:
                print('type:', tok.type,', value:',tok.value,", line:", tok.lineno,", column: ", tok.lexpos - breakLine[tok.lineno])

            if isFine:
                print("Analise lexica realizada com sucesso!")

            else:
                print("Analise lexica realizada com erro!")

if __name__ == "__main__":
    main()