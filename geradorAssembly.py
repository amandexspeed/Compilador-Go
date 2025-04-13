from visitorAbstract import visitorAbstract
from analiseSintatica import *
import AssemblyST as st
import struct

def getAssemblyType(type = None):
    # Apenas protótipo
    return ".word"

class geradorAssembly(visitorAbstract):
    def __init__(self):
        st.beginScope(st.SCOPE_MAIN) #Cria escopo main
        #funcs, text e data são listas que armazenam o código assembly

        """Registradores dedicados:
        
        $f0 e $f1: registradores para cálculos com ponto flutuante
        $f2 a $f12: registradores para variáveis temporárias (float)
        $f13: Registrador para resultados com float
        $t9 : resultado de expressões com os registradores de inteiros
        """

        self.registradoresPadroes = {

            "int": {"$t0", "$t1", "$t2", "$t3", "$t4"},
            "float": {"$f2", "$f3", "$f4", "$f5", "$f6", "$f7", "$f8", "$f9", "$f10", "$f11", "$f12"},
            "string":{"$t5", "$t6"},
            "bool": {"$t7","$t8"},
            "params": {"$a0", "$a1", "$a2", "$a3"},
        }

        self.contador = {"int": 0, "float": 0, "string": 0, "bool": 0, "params": 0} # Contador de variáveis temporárias
        self.limitesTipos = {"int": 5, "float": 10, "string": 2, "bool": 2, "params": 4}

        self.contGlobais = 0
        self.contSubstitutos = {"int": 0, "float": 0, "string": 0, "bool": 0, "params": 0}

        self.contOperacaoFloat = 0
        self.contadorFor = 0
        self.contadorWhile = 0
        self.contadorIf = 0

        self.funcs = []  
        self.text = []  
        self.text.append(".text")
        self.text.append("    move $fp, $sp")
        self.data = set()  # Campo .data
        self.rotulos = {}  #dicionario que armazena rotulos gerados para alguns comandos e expressoes (while, exppot) 
        self.byte_count = 0 # Contador de bytes para o campo .data

    def resolveTipoVariavel(self, variavel):
        tipo = st.getBindable(variavel)[st.TYPE]
        if(tipo in st.inteiro):
            return "int"
        elif(tipo in st.real):
            return "float"
        elif(tipo == st.STRING):
            return "string"
        elif(tipo == st.BOOL):
            return "bool"
        else:
            raise Exception(f"Tipo de variável desconhecido: {tipo}")

    def reajustarRegistrador(self, variavel):

        variavel
        tipo = self.resolveTipoVariavel(variavel)
        registradorNovo = self.escolhaRegistrador(variavel)

        


    def novo_rotulo(self, string):
        if not string in self.rotulos:
            self.rotulos[string] = 0
        rotulo = f"{string}_{self.rotulos[string]}"
        self.rotulos[string] += 1
        return rotulo
    
    #Devolve a lista de instruções que utilizada de acordo com o escopo
    def getList(self):
        return self.text if st.getScope() == st.SCOPE_MAIN else self.funcs    

    def escolhaRegistrador(self, variavel):
        if(variavel.__class__== sa.DeclaracaoExplicita):
            if (st.getScope() == st.SCOPE_MAIN) :
                if(self.contGlobais < 8):
                    return "$s"+str(++self.contGlobais)

        tipo = self.resolveTipoVariavel(variavel)
        if(self.limitesTipos[tipo] < self.contador[tipo]):
            registrador = self.registradoresPadroes[tipo][self.contador[tipo]]
            self.contador[tipo] += 1
            return registrador
        else: 
            registrador = self.registradoresPadroes[tipo][self.contadorSubstituto[tipo]]
            self.contadorSubstituto[tipo] = (self.contadorSubstituto[tipo]+1)%self.limitesTipos[tipo]
            return registrador
        
    def visitPrograma(self, programa):
        
        pre_visit = PreVisit()
        programa.accept(pre_visit)
        self.text.extend(pre_visit.text)
        self.data.update(pre_visit.data)
        self.byte_count = pre_visit.byte_count


        programa.pacote.accept(self)
        if(programa.importacao != None):
            programa.importacao.accept(self)
        if(programa.declaracaoExplicita != None ):
            programa.declaracaoExplicita.accept(self)
        if(programa.funcoes_codigo != None):
            programa.funcoes_codigo.accept(self)

    def visitPacote(self, pacote):
        pass

    def visitImportacaoSimples(self, importacao):
        pass

    def visitImportacaoComposta(self, importacao):
        pass

    def visitCodigo(self, codigo):
        for estrutura in codigo.listaEstruturas:
            estrutura.accept(self)

    def visitExpressaoAND(self, expressao):

        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)  # Avalia a primeira expressão
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]

    
        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"

        retorno = expressao.direita.accept(self)  # Avalia a segunda expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita != "bool" or tipo_Esquerda != "bool"):
            raise Exception("Operação AND só pode ser feita entre booleanos")

        code.append(f"    and $v0, {registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")

        return ("bool", "$v0")  # Retorna o tipo e o registrador da expressão

    def visitExpressaoOR(self, expressao):
        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)  # Avalia a primeira expressão
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]

    
        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"

        retorno = expressao.direita.accept(self)  # Avalia a segunda expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita != "bool" or tipo_Esquerda != "bool"):
            raise Exception("Operação or só pode ser feita entre booleanos")

        code.append(f"    or $v0, {registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")

        return ("bool", "$v0")  # Retorna o tipo e o registrador da expressão
    
    def visitExpressaoIGUAL(self, expressao):
        
        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)  # Avalia a primeira expressão
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]

    
        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"

        retorno = expressao.direita.accept(self)  # Avalia a segunda expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita == tipo_Esquerda):
            match tipo_Direita:
                case "int":
                    code.append(f"    seq $v0, {registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")
                
                case "float":
                    code.append(f"    c.eq.s {registradorEsquerda}, {registradorDireita}")
                    code.append(f"    bc1t Equals{self.contOperacaoFloat}")
                    code.append(f"    li $v0, 0")
                    code.append(f"    j EndEquals{self.contOperacaoFloat}")
                    code.append(f"Equals{self.contOperacaoFloat}:")
                    code.append(f"    li $v0, 1")
                    code.append(f"EndEquals{self.contOperacaoFloat}:")
                    self.contOperacaoFloat += 1

                case "string":
                    variavel = st.getBindableByRegister("$t9") 
                    if(variavel != None):
                        print("Registrador já utilizado")

                    """----------------IMPLEMENTAR COMPARAÇÃO DE STRINGS------------------------""" 
                    code.append(f"    la $v0, {registradorEsquerda}")
                    code.append(f"    la $v1, {registradorDireita}")
                    code.append(f"    li $t0, 0")
                    code.append(f"    lb $t0, 0($v0)")
                    code.append(f"    lb $t1, 0($v1)")
                    code.append(f"    beqz $t0, EndString{self.contOperacaoFloat}")
                    code.append(f"    beqz $t1, EndString{self.contOperacaoFloat}")
                    code.append(f"    beq $t0, $t1, EqualsString{self.contOperacaoFloat}")
                    code.append(f"    li $v0, 0")
                    code.append(f"    j EndEqualsString{self.contOperacaoFloat}")
                    code.append(f"EqualsString{self.contOperacaoFloat}:")
                    code.append(f"    li $v0, 1")
                    code.append(f"EndString{self.contOperacaoFloat}:")

                case "bool":
                    code.append(f"    seq $v0, {registradorEsquerda}, {registradorDireita}")  

                case _ :
                    raise Exception("Operação não suportada")  

        return ("bool", "$v0")  # Retorna o tipo e o registrador da expressão


    def visitExpressaoDIFFERENT(self, expressao):
        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)  # Avalia a primeira expressão
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]

        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9, $v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"
        
        retorno = expressao.direita.accept(self)  # Avalia a segunda expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita == tipo_Esquerda):
            match tipo_Direita:
                case "int":
                    code.append(f"    sne $v0, {registradorEsquerda}, {registradorDireita}")

                case "float":
                    code.append(f"    c.eq.s {registradorEsquerda}, {registradorDireita}")
                    code.append(f"    bc1t NotEquals{self.contOperacaoFloat}")
                    code.append(f"    li $v0, 1")
                    code.append(f"    j EndNotEquals{self.contOperacaoFloat}")
                    code.append(f"NotEquals{self.contOperacaoFloat}:")
                    code.append(f"    li $v0, 0")
                    code.append(f"EndNotEquals{self.contOperacaoFloat}:")
                    self.contOperacaoFloat += 1
                case "string":
                    variavel = st.getBindableByRegister("$t9")
                    if(variavel != None):
                        print("Registrador já utilizado")

                    """----------------IMPLEMENTAR COMPARAÇÃO DE STRINGS------------------------"""
                    code.append(f"    la $v0, {registradorEsquerda}")
                    code.append(f"    la $v1, {registradorDireita}")
                    code.append(f"    li $t0, 0")
                    code.append(f"    lb $t0, 0($v0)")
                    code.append(f"    lb $t1, 0($v1)")
                    code.append(f"    beqz $t0, EndString{self.contOperacaoFloat}")
                    code.append(f"    beqz $t1, EndString{self.contOperacaoFloat}")
                    code.append(f"    beq $t0, $t1, NotEqualsString{self.contOperacaoFloat}")
                    code.append(f"    li $v0, 0")
                    code.append(f"    j EndNotEqualsString{self.contOperacaoFloat}")
                    code.append(f"NotEqualsString{self.contOperacaoFloat}:")
                    code.append(f"    li $v0, 1")
                    code.append(f"EndString{self.contOperacaoFloat}:")

                case "bool":
                    code.append(f"    sne $v0, {registradorEsquerda}, {registradorDireita}")  

                case _ :
                    raise Exception("Operação não suportada")
                
            return ("bool", "$v0")  # Retorna o tipo e o registrador da expressão
    
    def visitExpressaoGREATER(self, expressao):
        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]
            

        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"
            
        retorno = expressao.direita.accept(self)  # Avalia a primeira expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita == tipo_Esquerda):
            match tipo_Direita:
                case "int":
                    code.append(f"    sgt $v0, {registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")
                case "float":
                    code.append(f"    c.lt.s {registradorEsquerda}, {registradorDireita}")
                    code.append(f"    bc1t Greater{self.contOperacaoFloat}")
                    code.append(f"    li $v0, 1")
                    code.append(f"    j EndGreater{self.contOperacaoFloat}")
                    code.append(f"Greater{self.contOperacaoFloat}:")
                    code.append(f"    li $v0, 0")
                    code.append(f"EndGreater{self.contOperacaoFloat}:")
                    self.contOperacaoFloat += 1
                case _ :
                    raise Exception("Operação não suportada")

        return ("bool", "$v0")  # Retorna o tipo e o registrador da expressão
    
    def visitExpressaoLESS(self, expressao):

        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)  # Avalia a primeira expressão
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]
            

        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"
            
        retorno = expressao.direita.accept(self)  # Avalia a primeira expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita == tipo_Esquerda):
            match tipo_Direita:
                case "int":
                    code.append(f"    slt $v0, {registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")
                case "float":
                    code.append(f"    c.lt.s {registradorEsquerda}, {registradorDireita}")
                    code.append(f"    bc1t Less{self.contOperacaoFloat}")
                    code.append(f"    li $v0, 0")
                    code.append(f"    j EndLess{self.contOperacaoFloat}")
                    code.append(f"Less{self.contOperacaoFloat}:")
                    code.append(f"    li $v0, 1")
                    code.append(f"EndLess{self.contOperacaoFloat}:")
                    self.contOperacaoFloat += 1
                case _ :
                    raise Exception("Operação não suportada")

        return ("bool", "$v0")  # Retorna o tipo e o registrador da expressão
    
    def visitExpressaoGREAT_OR_EQUAL(self, expressao):
        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]
            

        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"
            
        retorno = expressao.direita.accept(self)  # Avalia a primeira expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita == tipo_Esquerda):
            match tipo_Direita:
                case "int":
                    code.append(f"    sge $v0, {registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")
                case "float":
                    code.append(f"    c.le.s {registradorEsquerda}, {registradorDireita}")
                    code.append(f"    bc1t GreaterOrEqual{self.contOperacaoFloat}")
                    code.append(f"    li $v0, 1")
                    code.append(f"    j EndGreaterOrEqual{self.contOperacaoFloat}")
                    code.append(f"GreaterOrEqual{self.contOperacaoFloat}:")
                    code.append(f"    li $v0, 0")
                    code.append(f"EndGreaterOrEqual{self.contOperacaoFloat}:")
                    self.contOperacaoFloat += 1
                case _ :
                    raise Exception("Operação não suportada")

        return ("bool", "$v0")  # Retorna o tipo e o registrador da expressão
    
    def visitExpressaoLESS_OR_EQUAL(self, expressao):
        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]
            

        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"
            
        retorno = expressao.direita.accept(self)  # Avalia a primeira expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita == tipo_Esquerda):
            match tipo_Direita:
                case "int":
                    code.append(f"    sle $v0, {registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")
                case "float":
                    code.append(f"    c.le.s {registradorEsquerda}, {registradorDireita}")
                    code.append(f"    bc1t LessOrEqual{self.contOperacaoFloat}")
                    code.append(f"    li $v0, 0")
                    code.append(f"    j EndLessOrEqual{self.contOperacaoFloat}")
                    code.append(f"LessOrEqual{self.contOperacaoFloat}:")
                    code.append(f"    li $v0, 1")
                    code.append(f"EndLessOrEqual{self.contOperacaoFloat}:")
                    self.contOperacaoFloat += 1
                case _ :
                    raise Exception("Operação não suportada")

        return ("bool", "$v0")  # Retorna o tipo e o registrador da expressão
    
    def visitExpressaoSOMA(self, expressao):

        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]
            

        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"
            
        retorno = expressao.direita.accept(self)  # Avalia a primeira expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita == tipo_Esquerda):
            match tipo_Direita:
                case "int":
                    code.append(f"    add $v0, {registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")
                    return ("int", "$v0")  # Retorna o tipo e o registrador da expressão
                case "float":
                    code.append(f"    add.s $f13, {registradorEsquerda}, {registradorDireita}")
                    return ("float", "$f13")  # Retorna o tipo e o registrador da expressão
                case _ :
                    raise Exception("Operação não suportada")
    
    def visitExpressaoSUB(self, expressao):
        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]
            

        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"
            
        retorno = expressao.direita.accept(self)  # Avalia a primeira expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita == tipo_Esquerda):
            match tipo_Direita:
                case "int":
                    code.append(f"    sub $v0, {registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")
                    return ("int", "$v0")  # Retorna o tipo e o registrador da expressão
                case "float":
                    code.append(f"    sub.s $f13, {registradorEsquerda}, {registradorDireita}")
                    return ("float", "$f13")  # Retorna o tipo e o registrador da expressão
                case _ :
                    raise Exception("Operação não suportada")
    
    def visitExpressaoMULT(self, expressao):
        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]
            

        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"
            
        retorno = expressao.direita.accept(self)  # Avalia a primeira expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita == tipo_Esquerda):
            match tipo_Direita:
                case "int":
                    code.append(f"    mul $v0, {registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")
                    return ("int", "$v0")  # Retorna o tipo e o registrador da expressão
                case "float":
                    code.append(f"    mul.s $f13, {registradorEsquerda}, {registradorDireita}")
                    return ("float", "$f13")  # Retorna o tipo e o registrador da expressão
                case _ :
                    raise Exception("Operação não suportada")
    
    def visitExpressaoMOD(self, expressao):

        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]
            

        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"
            
        retorno = expressao.direita.accept(self)  # Avalia a primeira expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita == tipo_Esquerda):
            match tipo_Direita:
                case "int":
                    code.append(f"    div {registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")
                    code.append(f"    mfhi $v0")
                    return ("int", "$v0")  # Retorna o tipo e o registrador da expressão
                case "float":
                    code.append(f"    div.s $f14, {registradorEsquerda}, {registradorDireita}")
                    code.append(f"    floor.s $f14, $f14")
                    code.append(f"    mul.s $f15, $f14, {registradorDireita}")
                    code.append(f"    sub.s $f13, {registradorEsquerda}, $f15")
                    return ("float", "$f13")  # Retorna o tipo e o registrador da expressão
                case _ :
                    raise Exception("Operação não suportada")
    
    def visitExpressaoDIV(self, expressao):
        code = self.getList()
        registradorEsquerda = None
        registradorDireita = None
        tipo_Direita = None
        tipo_Esquerda = None

        retorno = expressao.esquerda.accept(self)
        registradorEsquerda = retorno[1]  # Armazena o resultado
        tipo_Esquerda = retorno[0]
            

        if(registradorEsquerda == "$v0"):
            code.append("    lw $t9,$v0")# Muda registrador da expressão da direita pra n ser sobrescrito
            registradorEsquerda = "$t9"
            
        retorno = expressao.direita.accept(self)  # Avalia a primeira expressão
        registradorDireita = retorno[1]  # Armazena o resultado
        tipo_Direita = retorno[0]

        if(tipo_Direita == tipo_Esquerda):
            match tipo_Direita:
                case "int":
                    code.append(f"    div $v0,{registradorEsquerda}, {registradorDireita}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")
                    return ("int", "$v0")  # Retorna o tipo e o registrador da expressão
                case "float":
                    code.append(f"    div.s $f13, {registradorEsquerda}, {registradorDireita}")
                    return ("float", "$f13")  # Retorna o tipo e o registrador da expressão
                case _ :
                    raise Exception("Operação não suportada")
    
    def visitExpressaoNEGATION(self, expressao):

        code = self.getList()
        registrador = None
        tipo = None

        retorno = expressao.operando.accept(self)  # Avalia a primeira expressão
        registrador = retorno[1]  # Armazena o resultado
        tipo = retorno[0]

        if(tipo != "bool"):
            raise Exception("Operação NOT só pode ser feita com booleanos")

        code.append(f"    sub $v0, $zero, {registrador}")  # Se registrador da esquerda < Registrador da direita, então $t0 = 1, senão $t0 = 0")

        return ("bool", "$v0")  # Retorna o tipo e o registrador da expressão
    
    def visitExpressaoINCREMENTO(self, expressao):
        code = self.getList()
        registrador = st.getBindable(expressao.id)[st.REGISTRADOR]
        if(self.resolveTipoVariavel(expressao.id) != "int"):
            raise Exception("Operação só pode ser feita com inteiros")
        code.append(f" addi {registrador}, {registrador}, 1")
        return ("int", {registrador})

    def visitExpressaoPRE_INCREMENTO(self, expressao):
            code = self.getList()
            registrador = st.getBindable(expressao.id)[st.REGISTRADOR]
            if(self.resolveTipoVariavel(expressao.id) != "int"):
                raise Exception("Operação só pode ser feita com inteiros")
            code.append(f" addi {registrador}, {registrador}, 1")
            return ("int", {registrador})

    def visitExpressaoDECREMENTO(self, expressao):
        code = self.getList()
        registrador = st.getBindable(expressao.id)[st.REGISTRADOR]
        if(self.resolveTipoVariavel(expressao.id) != "int"):
            raise Exception("Operação só pode ser feita com inteiros")
        code.append(f" subi {registrador}, {registrador}, 1")
        return ("int", {registrador})

    def visitExpressaoPRE_DECREMENTO(self, expressao):
        code = self.getList()
        registrador = st.getBindable(expressao.id)[st.REGISTRADOR]
        if(self.resolveTipoVariavel(expressao.id) != "int"):
            raise Exception("Operação só pode ser feita com inteiros")
        code.append(f" subi {registrador}, {registrador}, 1")
        return ("int", {registrador})

    
    def visitConstanteConcreto(self, constante):

        code = self.getList()
        registrador = None
        tipo = None
        match constante.tipo:
            case "int":
                code.append(f"    li $v0, {constante.valor}")
                registrador = "$v0"
                tipo_Esquerda = "int"

            case "float":
                hex_value = struct.unpack('>I', struct.pack('>f', constante.valor))[0]
                code.append(f"    lw $v0, {hex_value}")
                code.append(f"    mtc1 $v0, $f0")
                registrador = "$f0"
                tipo = "float"

            case "string":
                code.append(f"    la $v0, {constante.valor}")
                registrador = "$v0"
                tipo = "string"

            case "bool":
                valor = 1 if constante.valor=="TRUE" else 0
                code.append(f"    li $v0, {valor}")
                registrador = "$v0"
                tipo = "bool"

            case "ID":
                registradorEsquerda = st.getBindable(constante.valor)[st.REGISTRADOR]
                if(registradorEsquerda == None):
                    st.alocarVariavel(constante.valor, self.escolhaRegistrador(constante.tipo, constante))
                    registrador = st.getBindable(constante.valor)[st.REGISTRADOR]
                    tipo = self.resolveTipoVariavel(constante.valor)
                    """case "id":
                    code = self.getList() 
                    idName = st.getBindable(constante.id)
                    if (idName != None):
                    if (st.getScope(constante.id) == st.SCOPE_MAIN):
                        code.append(f"    lw $v0, {constante.id}($zero)")
                    else:
                        code.append(f"    lw $v0, {idName[st.OFFSET]}($fp)")"""
                        
        return (tipo, registrador)

    def visitExpressaoPARENTESE(self, expressao):
        return expressao.expressao.accept(self)

    def visitAssignPlus(self, expMatRedu):
        code = self.getList()
        registrador = st.getBindable(expMatRedu.id)[st.REGISTRADOR]
        retorno = expMatRedu.exp.accept(self)
        code.append(f" add {registrador}, {registrador}, {retorno[1]}")
        code.append(f" move $v0, {registrador}")
        return ("int", "$v0")

    def visitAssignMinus(self, expMatRedu):
        code = self.getList()
        registrador = st.getBindable(expMatRedu.id)[st.REGISTRADOR]
        retorno = expMatRedu.exp.accept(self)
        code.append(f" sub {registrador}, {registrador}, {retorno[1]}")
        code.append(f" move $v0, {registrador}")
        return ("int", "$v0")

    def visitAssignMult(self, expMatRedu):
        code = self.getList()
        registrador = st.getBindable(expMatRedu.id)[st.REGISTRADOR]
        retorno = expMatRedu.exp.accept(self)
        code.append(f" mul {registrador}, {registrador}, {retorno[1]}")
        code.append(f" move $v0, {registrador}")
        return ("int", "$v0")

    def visitAssignDiv(self, expMatRedu):
        code = self.getList()
        registrador = st.getBindable(expMatRedu.id)[st.REGISTRADOR]
        retorno = expMatRedu.exp.accept(self)
        code.append(f" div {registrador}, {registrador}, {retorno[1]}")
        code.append(f" mflo {registrador}")
        code.append(f" move $v0, {registrador}")
        return ("int", "$v0")

    
    def visitFor_CLIKEconcrete(self, estruturaFor):
        code = self.getList()
        rotulo_inicio = self.novo_rotulo("forCLIKE_inicio")
        rotulo_fim = self.novo_rotulo("forCLIKE_fim")

        # Inicialização do loop
        estruturaFor.declaracao.accept(self)

        code.append(f"{rotulo_inicio}:")
        # Condição do loop
        retorno = estruturaFor.expressao1.accept(self)
        code.append(f" beq {retorno[1]}, $zero, {rotulo_fim}")

        # Corpo do loop
        estruturaFor.codigo.accept(self)

        # Incremento do loop
        estruturaFor.expressao2.accept(self)
        code.append(f" j {rotulo_inicio}")
        code.append(f"{rotulo_fim}:")

    
    def visitFor_INFINITOconcrete(self, EstruturaFOR):
        code = self.getList()
        rotulo_inicio = self.novo_rotulo("forInf_inicio")
        rotulo_fim = self.novo_rotulo("forInf_fim")

        code.append(f"{rotulo_inicio}:")

        # Corpo do loop
        EstruturaFOR.codigo.accept(self)

        code.append(f" j {rotulo_inicio}")
        code.append(f"{rotulo_fim}:")

    def visitFor_WHILEconcrete(self, EstruturaFOR):
        code = self.getList()
        rotulo_inicio = self.novo_rotulo("forWHILE_inicio")
        rotulo_fim = self.novo_rotulo("forWHILE_fim")

        code.append(f"{rotulo_inicio}:")
        # Condição do loop
        retorno = EstruturaFOR.expressao.accept(self)
        code.append(f" beq {retorno[1]}, $zero, {rotulo_fim}")

        # Corpo do loop
        EstruturaFOR.codigo.accept(self)

        code.append(f" j {rotulo_inicio}")
        code.append(f"{rotulo_fim}:")


    def visitEstruturaIFconcrete(self, estruturaIf):
        code = self.getList()
        rotulo_fim = self.novo_rotulo("if_fim")

        # Condição do if
        retorno = estruturaIf.expressao.accept(self)
        code.append(f" beq {retorno[1]}, $zero, {rotulo_fim}")

        # Corpo do if
        estruturaIf.codigo.accept(self)
        code.append(f"{rotulo_fim}:")


    def visitEstruturaIF_ELSEconcrete(self, estruturaElse):
        code = self.getList()
        rotulo_else = self.novo_rotulo("else")
        rotulo_fim = self.novo_rotulo("if_fim")

        # Condição do if
        retorno = estruturaElse.expressao.accept(self)
        code.append(f" beq {retorno[1]}, $zero, {rotulo_else}")

        # Corpo do if
        estruturaElse.codigo.accept(self)
        code.append(f" j {rotulo_fim}")

        # Corpo do else
        code.append(f"{rotulo_else}:")
        estruturaElse.expressao_else.accept(self)
        code.append(f"{rotulo_fim}:")

    
    def visitEstruturaELSEconcrete(self, estruturaElse):
        code = self.getList()
        rotulo_fim = self.novo_rotulo("else_fim")

        # Corpo do else
        estruturaElse.codigo.accept(self)
        code.append(f"{rotulo_fim}:")

    
    def visitEstruturaELSE_IFconcrete(self, estruturaElseIf):
        code = self.getList()
        rotulo_else_if = self.novo_rotulo("else_if")
        rotulo_fim = self.novo_rotulo("if_fim")

        # Condição do if
        retorno = estruturaElseIf.estrutura_if.expressao.accept(self)
        code.append(f" beq {retorno[1]}, $zero, {rotulo_else_if}")

        # Corpo do if
        estruturaElseIf.estrutura_if.codigo.accept(self)
        code.append(f" j {rotulo_fim}")

        # Corpo do else if
        code.append(f"{rotulo_else_if}:")
        estruturaElseIf.estrutura_if.expressao_else.accept(self)
        code.append(f"{rotulo_fim}:")

    
    def visitFuncao(self, funcao):
        st.addFunction(funcao.id, funcao.tipo, funcao.parametros, funcao.codigo)
        code = self.getList()
        rotulo_funcao = self.novo_rotulo(funcao.id)
        code.append(f"{rotulo_funcao}:")
        if(funcao.lista_parametros != None):
            parametros = st.getBindable(funcao.id)[st.PARAMS]
            for i in range(len(parametros)):
                st.addExplicitVariable(parametros[i][0], parametros[i][1],self.escolhaRegistrador(parametros[i][1]))
        funcao.codigo.accept(self)
        st.endScope()

    def visitRetornoFuncao(self, retorno):
        pass

    def visitAtribuicao(self, Atribuicao):
        pass

    def visitDeclaracaoExplicitaSimples(self, DeclaracaoExplicitaSimples):
        pass

    def visitDeclaracaoExplicitaEmListaSimples(self, DeclaracaoExplicita):
        pass

    def visitDeclaracaoExplicitaComposta(self, DeclaracaoExplicita):
        pass

    def visitDeclaracaoCurta(self, DeclaracaoCurta):
        pass

    def visitParametroSimples(self, Parametro):
        pass

    def visitParametroCompostoTipoUnico(self, ParametroComposto):
        pass

    def visitParametroCompostoVariosTipos(self, ParametroComposto):
        pass

    def visitChamadaFuncao(self, ChamadaFuncao):
        pass

    #gera código assembly
    def get_code(self):
        finalcode = []
        if self.data:
            for globalVar in self.data:
                finalcode.insert(0, f"    {globalVar[0]}: {globalVar[1]} 0")
            finalcode.insert(0,".data")
        finalcode = finalcode + self.text
        finalcode.append("    j end")
        finalcode = finalcode + self.funcs
        finalcode.append("\nend:\n    li $v0, 10\n    syscall")
        return "\n".join(finalcode)
    
class PreVisit(visitorAbstract):
    def __init__(self):
        self.data = []
        self.text = []
        self.byte_count = 0

    def visitPrograma(self, programa):
        programa.pacote.accept(self)
        if programa.importacao is not None:
            programa.importacao.accept(self)
        if programa.declaracaoExplicita is not None:
            programa.declaracaoExplicita.accept(self)
        if programa.funcoes_codigo is not None:
            programa.funcoes_codigo.accept(self)

    def visitPacote(self, pacote):
        pass

    def visitImportacaoSimples(self, importacao):
        pass

    def visitImportacaoComposta(self, importacao):
        pass

    def visitCodigo(self, codigo):
        for estrutura in codigo.listaEstruturas:
            estrutura.accept(self)

    def visitExpressaoAND(self, expressao):
        pass

    def visitExpressaoOR(self, expressao):
        pass

    def visitExpressaoIGUAL(self, expressao):
        pass

    def visitExpressaoDIFFERENT(self, expressao):
        pass

    def visitExpressaoGREATER(self, expressao):
        pass

    def visitExpressaoLESS(self, expressao):
        pass

    def visitExpressaoGREAT_OR_EQUAL(self, expressao):
        pass

    def visitExpressaoLESS_OR_EQUAL(self, expressao):
        pass

    def visitExpressaoSOMA(self, expressao):
        pass

    def visitExpressaoSUB(self, expressao):
        pass

    def visitExpressaoMULT(self, expressao):
        pass

    def visitExpressaoMOD(self, expressao):
        pass

    def visitExpressaoDIV(self, expressao):
        pass

    def visitExpressaoNEGATION(self, expressao):
        pass

    def visitExpressaoINCREMENTO(self, expressao):
        pass

    def visitExpressaoPRE_INCREMENTO(self, expressao):
        pass

    def visitExpressaoDECREMENTO(self, expressao):
        pass

    def visitExpressaoPRE_DECREMENTO(self, expressao):
        pass

    def visitConstanteConcreto(self, constante):
        tipo = constante.tipo
        valor = constante.valor
        if tipo == "string":
            self.text.append(f"{valor}: .asciiz \"{valor}\"")
            self.byte_count += len(valor) + 1  # +1 para o caractere nulo
        else:
            self.data.append(f"{valor}: .word {valor}")
            self.byte_count += 4  # 4 bytes para inteiros e floats

    def visitExpressaoPARENTESE(self, expressao):
        pass

    def visitAssignPlus(self, expMatRedu):
        pass

    def visitAssignMinus(self, expMatRedu):
        pass

    def visitAssignMult(self, expMatRedu):
        pass

    def visitAssigndiv(self, expMatRedu):
        pass

    def visitFor_CLIKEconcrete(self, EstruturaFOR):
        pass

    def visitFor_INFINITOconcrete(self, EstruturaFOR):
        pass

    def visitFor_WHILEconcrete(self, EstruturaFOR):
        pass

    def visitEstruturaIFconcrete(self, estruturaIf):
        pass

    def visitEstruturaIF_ELSEconcrete(self, estruturaElse):
        pass

    def visitEstruturaELSEconcrete(self, estruturaElse):
        pass

    def visitEstruturaELSE_IFconcrete(self, estruturaElse):
        pass

    def visitFuncao(self, funcao):
        pass

    def visitRetornoFuncao(self, retorno):
        pass

    def visitAtribuicao(self, Atribuicao):
        pass

    def visitDeclaracaoExplicitaSimples(self, DeclaracaoExplicitaSimples):
        tipo = DeclaracaoExplicitaSimples.tipo
        nome = DeclaracaoExplicitaSimples.nomeVariavel
        valor = DeclaracaoExplicitaSimples.valor
        if tipo == "string":
            self.text.append(f"{nome}: .asciiz \"{valor}\"")
            self.byte_count += len(valor) + 1  # +1 para o caractere nulo
        else:
            self.data.append(f"{nome}: .word {valor}")
            self.byte_count += 4  # 4 bytes para inteiros e floats

    def visitDeclaracaoExplicitaEmListaSimples(self, declaracao):
        for nome, valor in zip(declaracao.listaVariaveis, declaracao.listaExpressoes):
            tipo = declaracao.tipo
            if tipo == "string":
                self.text.append(f"{nome}: .asciiz \"{valor}\"")
                self.byte_count += len(valor) + 1  # +1 para o caractere nulo
            else:
                self.data.append(f"{nome}: .word {valor}")
                self.byte_count += 4  # 4 bytes para inteiros e floats

    def visitConstanteConcreto(self, constante):
        tipo = constante.tipo
        valor = constante.valor
        if tipo == "string":
            self.text.append(f"{valor}: .asciiz \"{valor}\"")
            self.byte_count += len(valor) + 1  # +1 para o caractere nulo
        else:
            self.data.append(f"{valor}: .word {valor}")
            self.byte_count += 4  # 4 bytes para inteiros e floats

    def get_code(self):
        finalcode = []
        if self.data:
            finalcode.append(".data")
            finalcode.extend(self.data)
        if self.text:
            finalcode.append(".text")
            finalcode.extend(self.text)
        return "\n".join(finalcode), self.byte_count
