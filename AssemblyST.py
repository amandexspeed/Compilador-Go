#Dicionario que representa a tabela de simbolos.
symbolTable = []

registerTable = []

INT = 'int'
INT8 = 'int8'
INT16 = 'int16'
INT32 = 'int32'
INT64 = 'int64'
FLOAT32 = 'float32'
FLOAT64 = 'float64'
BOOL = 'boolean'
TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'fun'
EXPLICITVARIABLE = 'expvar'
MUTABLEVARIABLE = 'mutvar' 
SCOPE = 'scope'
SCOPE_MAIN = 'main'
OFFSET = 'offset'
SP = 'sp'
REGISTER = 'register'

# Se DEBUG = -1, imprime conteudo da tabela de símbolos após cada mudança
DEBUG = 0
Numero = [INT, INT8, INT16, INT32, INT64, FLOAT32, FLOAT64]
inteiro = [INT, INT8, INT16, INT32, INT64]
real = [FLOAT32, FLOAT64]


def printTable():
    global DEBUG
    if DEBUG == -1:
        print('Tabela:', symbolTable)

def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope
    symbolTable[-1][SP] = 0
    printTable()

def endScope():
    global symbolTable
    symbolTable = symbolTable[0:-1]
    printTable()
"""
def addVar(name, type):
    global symbolTable
    if not name in symbolTable[-1]:
        symbolTable[-1][SP] -= 4 
        symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE : type, OFFSET: symbolTable[-1][SP]}
    else:
        symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE : type, OFFSET: symbolTable[-1][name][OFFSET]}
    printTable()

"""

def addMultableVariable(nome, tipo, registrador):
    global symbolTable
    global registerTable

    if registrador in registerTable:
        print("Registrador já utilizado")
        getBindableByRegister(registrador)[REGISTER] = None
    
    registerTable[registrador] = nome

    if not nome in symbolTable[-1]:
        symbolTable[-1][SP] -= 4
        symbolTable[-1][nome] = {BINDABLE: MUTABLEVARIABLE, TYPE: tipo, OFFSET: symbolTable[-1][SP], REGISTER: registrador}
    else:
        symbolTable[-1][nome] = {BINDABLE: MUTABLEVARIABLE, TYPE: tipo, OFFSET: symbolTable[-1][nome][OFFSET], REGISTER: registrador}


    printTable()

def addExplicitVariable(nome, tipo,registrador):
    global symbolTable

    global registerTable

    if registrador in registerTable:
        print("Registrador já utilizado")
        getBindableByRegister(registrador)[REGISTER] = None
    
    registerTable[registrador] = nome

    if not nome in symbolTable[-1]:
        symbolTable[-1][SP] -= 4
        symbolTable[-1][nome] = {BINDABLE: EXPLICITVARIABLE, TYPE: tipo, OFFSET: symbolTable[-1][SP], REGISTER: registrador}
    else:
        symbolTable[-1][nome] = {BINDABLE: MUTABLEVARIABLE, TYPE: tipo, OFFSET: symbolTable[-1][nome][OFFSET], REGISTER: registrador}
    printTable()

def alocarVariavel(nome, registrador):
    global symbolTable
    global registerTable

    if not nome in symbolTable[-1]:
        raise Exception("Variável não encontrada")
    
    if registrador in registerTable:
        print("Registrador já utilizado")
        getBindableByRegister(registrador)[REGISTER] = None

    registerTable[registrador] = nome

    symbolTable[-1][nome][REGISTER] = registrador
    printTable()

def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE : returnType}
    printTable()

def addSP(value):
    global symbolTable
    symbolTable[-1][SP] += value
    

def getSP():
    return symbolTable[-1][SP]

def getBindableByRegister(registrador):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (registrador in symbolTable[i].values()):
            return symbolTable[i][-1][registrador]
    return None

def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None

def getScope(bindableName = None):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][SCOPE]
        else:
            return symbolTable[-1][SCOPE]
    return None


def main():
    global DEBUG
    DEBUG = -1
   

if __name__ == "__main__":
    main()