from visitorAbstract import visitorAbstract
from analiseSintatica import *
import AssemblyST as st

def getAssemblyType(type = None):
    # Apenas protótipo
    return ".word"

class geradorAssembly(visitorAbstract):
    def __init__(self):
        st.beginScope(st.SCOPE_MAIN) #Cria escopo main
        #funcs, text e data são listas que armazenam o código assembly
        self.funcs = []  
        self.text = []  
        self.text.append(".text")
        self.text.append("    move $fp, $sp")
        self.data = set()  # Campo .data
        self.rotulos = {}  #dicionario que armazena rotulos gerados para alguns comandos e expressoes (while, exppot) 

    def novo_rotulo(self, string):
        if not string in self.rotulos:
            self.rotulos[string] = 0
        rotulo = f"{string}_{self.rotulos[string]}"
        self.rotulos[string] += 1
        return rotulo
    
    #Devolve a lista de instruções que utilizada de acordo com o escopo
    def getList(self):
        return self.text if st.getScope() == st.SCOPE_MAIN else self.funcs    

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
        pass
    
    def visitExpressaoDIFFERENT(self, expressao):
        pass
    
    def visitExpressaoGREATER(self, expressao):
        pass
    
    def visitExpressaoLESS(self, expressao):
        code = self.getList()
        # Avalia a primeira expressão e armazena na pilha
        expressao.esquerda.accept(self)
        code.append("    addi $sp, $sp, -4")
        st.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        # Avalia a segunda expressão
        expressao.direita.accept(self)
        # Recupera o primeiro operando
        code.append("    lw $t0, 0($sp)")
        code.append("    add $sp, $sp, 4")  # Libera espaço na pilha
        st.addSP(4)
        # Comparação: se $t0 < $v0, então $v0 = 1, senão $v0 = 0
        code.append("    slt $v0, $t0, $v0")
    
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

        match constante.tipo:
            case "int":
                code = self.getList()
                code.append(f"    li $v0, {constante.valor}")
            case "string":
                code = self.getList()
                code.append(f"    la $v0, {constante.valor}")
            case "bool":
                code = self.getList() 
                value = 1 if booleanExp.boolValue == "true" else 0
                code.append(f"    li $v0, {value}")
            case "id":
                code = self.getList() 
                idName = st.getBindable(constante.id)
                if (idName != None):
                    if (st.getScope(constante.id) == st.SCOPE_MAIN):
                        code.append(f"    lw $v0, {constante.id}($zero)")
                    else:
                        code.append(f"    lw $v0, {idName[st.OFFSET]}($fp)")
    
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