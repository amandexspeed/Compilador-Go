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

        self.funcs = []  
        self.text = []  
        self.text.append(".text")
        self.text.append("    move $fp, $sp")
        self.data = set()  # Campo .data
        self.rotulos = {}  #dicionario que armazena rotulos gerados para alguns comandos e expressoes (while, exppot) 

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
        pass

    def visitExpressaoOR(self, expressao):
        pass
    
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

        return ("int", "$v0")  # Retorna o tipo e o registrador da expressão


    def visitExpressaoDIFFERENT(self, expressao):
        pass
    
    def visitExpressaoGREATER(self, expressao):
        pass
    
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
                    code.append(f"    c.le.s {registradorEsquerda}, {registradorDireita}")
                    code.append(f"    bc1t Less{self.contOperacaoFloat}")
                    code.append(f"    li $v0, 0")
                    code.append(f"    j EndLess{self.contOperacaoFloat}")
                    code.append(f"Less{self.contOperacaoFloat}:")
                    code.append(f"    li $v0, 1")
                    code.append(f"EndLess{self.contOperacaoFloat}:")
                    self.contOperacaoFloat += 1
                case _ :
                    raise Exception("Operação não suportada")

        return ("int", "$v0")  # Retorna o tipo e o registrador da expressão
    
    def visitExpressaoGREAT_OR_EQUAL(self, expressao):
        pass
    
    def visitExpressaoLESS_OR_EQUAL(self, expressao):
        pass
    
    def visitExpressaoSOMA(self, expressao):
        code = self.getList()
        expressao.esquerda.accept(self)  # Avalia a primeira expressão
        code.append("    addi $sp, $sp, -4")  # Aloca espaço na pilha
        st.addSP(-4)
        code.append("    sw $v0, 0($sp)")  # Empilha o resultado
        expressao.direita.accept(self)  # Avalia a segunda expressão
        code.append("    lw $t0, 0($sp)")  # Recupera o valor salvo
        code.append("    add $sp, $sp, 4")  # Libera espaço da pilha
        st.addSP(4)
        code.append("    add $v0, $t0, $v0")  # Soma os valores
    
    def visitExpressaoSUB(self, expressao):
        code = self.getList()
        expressao.esquerda.accept(self)  # Avalia a primeira expressão
        code.append("    addi $sp, $sp, -4")  # Aloca espaço na pilha
        st.addSP(-4)
        code.append("    sw $v0, 0($sp)")  # Empilha o resultado
        expressao.direita.accept(self)  # Avalia a segunda expressão
        code.append("    lw $t0, 0($sp)")  # Recupera o valor salvo
        code.append("    add $sp, $sp, 4")  # Libera espaço da pilha
        st.addSP(4)
        code.append("    sub $v0, $t0, $v0")  # Subtrai os valores
    
    def visitExpressaoMULT(self, expressao):
        code = self.getList()        
        expressao.esquerda.accept(self)  # Avalia a primeira expressão
        code.append("    addi $sp, $sp, -4")
        st.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        expressao.direita.accept(self)  # Avalia a segunda expressão
        code.append("    lw $t0, 0($sp)")
        code.append("    add $sp, $sp, 4")
        st.addSP(4)   
        code.append("    mul $v0, $t0, $v0")  # Multiplica os valores
    
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

    def visitEstruturaIF_ELSEconcrete (self, estruturaElse):
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