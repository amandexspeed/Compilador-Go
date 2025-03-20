tabelaDesimbolos = []
INT = 'int'
INT8 = 'int8'
INT16 = 'int16'
INT32 = 'int32'
INT64 = 'int64'
FLOAT32 = 'float32'
FLOAT64 = 'float64'
BOOL = 'boolean'
STRING = 'string'
TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'fun'
SCOPE = 'scope'
EXPLICITVARIABLE = 'expvar'
MUTABLEVARIABLE = 'mutvar' 

DEBUG = -1

Numero = [INT, INT8, INT16, INT32, INT64, FLOAT32, FLOAT64]

def printTable():
    global DEBUG
    if DEBUG == -1:
        print('Tabela:', tabelaDesimbolos)

def beginScope(nomeEscopo):
    global tabelaDesimbolos
    tabelaDesimbolos.append({})
    tabelaDesimbolos[-1][SCOPE] = nomeEscopo
    printTable()

def endScope():
    global tabelaDesimbolos
    tabelaDesimbolos = tabelaDesimbolos[0:-1]
    printTable()

def addMultableVariable(nome, tipo):
    global tabelaDesimbolos
    tabelaDesimbolos[-1][nome] = {BINDABLE: MUTABLEVARIABLE, TYPE: tipo}
    printTable()

def addExplicitVariable(nome, tipo):
    global tabelaDesimbolos
    tabelaDesimbolos[-1][nome] = {BINDABLE: EXPLICITVARIABLE, TYPE: tipo}
    printTable()

def addFunction(nome, tipoRetorno, parametros):
    global tabelaDesimbolos
    tabelaDesimbolos[-1][nome] = {BINDABLE: FUNCTION, TYPE: tipoRetorno, PARAMS: parametros}
    printTable()

def getBindable(nome):
    global tabelaDesimbolos
    for i in reversed(range(len(tabelaDesimbolos))):
        if(nome in tabelaDesimbolos[i]):
            return tabelaDesimbolos[i][nome]
    return None

def main():
    global DEBUG
    DEBUG = -1
    print('\n# Criando escopo main')
    beginScope('main')
    print ('\n# Adicionando Vinculavel funcao some')
    addFunction('some', ['a', INT, 'b', INT], INT)

    print('\n# Criando escopo some')
    beginScope('some')

    print('\n# Adicionando var a do tipo int')
    addExplicitVariable('a', INT)
    print('\n# Adicionando var b do tipo int')
    addExplicitVariable('b', INT)
    print('\n# Adicionando c(de forma curta) do tipo int')
    addMultableVariable('c', INT)

    print('\n# Consultando bindable')
    print(str(getBindable('sumparabola')))
    print('\n# Consultando bindable')
    print(str(getBindable('some')))
    print('\n# Consultando bindable')
    print(str(getBindable('a')))
    print('\n# Consultando bindable')
    print(str(getBindable('c')))

    print('\n# Removendo escopo some')
    endScope()

if __name__ == "__main__":
    main()