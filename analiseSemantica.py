from visitor import *
import tabelaSimbolos as ts

global nomeArquivo
global nomePacote

class AnaliseSemantica(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        ts.beginScope('global' + nomeArquivo)

    def visitPrograma(self, programa):
        programa.pacote.accept(self)
        if(programa.importacao != None):
            programa.importacao.accept(self)
        if(programa.declaracaoExplicita != None ):
            programa.declaracaoExplicita.accept(self)
        
        RegistradorDeFuncao(programa).registraFuncoes()

        if(programa.funcoes_codigo != None):
            programa.funcoes_codigo.accept(self)

    def visitPacote(self, pacote):
        ts.beginScope(pacote.nome)
        global nomePacote
        nomePacote = pacote.nome

    def visitImportacaoSimples(self, importacao):
        pass

    @abstractmethod
    def visitImportacaoComposta(self, importacao):
        pass

    def visitCodigo(self, codigo):
        pass

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
        pass
    
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

    def visitRetornoFuncao(self, retorno):
        pass

class RegistradorDeFuncao():
    def __init__(self,programa):
        self.programa = programa
    
    def registraFuncoes(self):
        if(self.programa.funcoes_codigo != None):
            self.programa.funcoes_codigo.accept(self)

    def visitFuncaoCodigoConcrete(self, funcoes):
        for funcao in funcoes.listaFuncoes:
            funcao.accept(self)

    def visitFuncaoConcrete(self, funcao):

        if(ts.getBindable(funcao.nome) != None):
            print("Função " + funcao.nome + " já declarada")
        else:
            params = None
            if(funcao.lista_parametros != None):
                params = funcao.lista_parametros.accept(self)
            ts.addFunction(funcao.nome, funcao.tipoRetorno, params)

    def visitParametroSimples(self, Parametro):
        if(ts.getBindable(Parametro.nome) != None):
            print("Parametro " + Parametro.nome + " já declarado")
        else:
            return [[Parametro.nome, Parametro.tipo]]

    def visitParametroCompostoTipoUnico(self, ParametroComposto):
        listaParams = []
        for _ in ParametroComposto.identificadores:
            if(ts.getBindable(_.nome) != None):
                print("Parametro " + _.nome + " já declarado")
            else:
                listaParams.append([_.nome, ParametroComposto.tipo])
        return listaParams

    def visitParametroCompostoVariosTipos(self, ParametroComposto):
        listaParams = []
        for _ in ParametroComposto.Parametros:
            resposta = _.accept(self)
            if(ts.getBindable(resposta[0][0]) != None):
                print("Parametro " + resposta[0][0] + " já declarado")
            listaParams += resposta[0]
        return listaParams