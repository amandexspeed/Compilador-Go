from abc import ABCMeta, abstractmethod

class AbstractVisitor(metaclass = ABCMeta):

    @abstractmethod
    def visitPacote(self, pacote):
        pass

    @abstractmethod
    def visitImportacaoSimples(self, importacao):
        pass

    @abstractmethod
    def visitImportacaoComposta(self, importacao):
        pass

    @abstractmethod
    def visitCodigo(self, codigo):
        pass

    @abstractmethod
    def visitExpressaoAND(self, expressao):
        pass

    @abstractmethod
    def visitExpressaoOR(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoIGUAL(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoDIFFERENT(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoGREATER(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoLESS(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoGREAT_OR_EQUAL(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoLESS_OR_EQUAL(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoSOMA(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoSUB(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoMULT(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoMOD(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoDIV(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoNEGATION(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoINCREMENTO(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoPRE_INCREMENTO(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoDECREMENTO(self, expressao):
        pass
    
    @abstractmethod
    def visitExpressaoPRE_DECREMENTO(self, expressao):
        pass
    
    @abstractmethod
    def visitConstanteConcreto(self, constante):
        pass
    
    @abstractmethod
    def visitExpressaoPARENTESE(self, expressao):
        pass
   
    @abstractmethod
    def visitAssignPlus(self, expMatRedu):
       pass

    @abstractmethod
    def visitAssignMinus(self, expMatRedu):
       pass

    @abstractmethod
    def visitAssignMult(self, expMatRedu):
       pass

    @abstractmethod
    def visitAssigndiv(self, expMatRedu):
       pass

    @abstractmethod
    def visitEstruturaIF_ELSEconcrete (self, estruturaElse):
        pass
    
    @abstractmethod
    def visitEstruturaELSEconcrete(self, estruturaElse):
        pass
    
    @abstractmethod
    def visitEstruturaELSE_IFconcrete(self, estruturaElse):
        pass
    
    @abstractmethod
    def visitFor_CLIKEconcrete(self, EstruturaFOR):
        pass
    
    @abstractmethod
    def visitFor_INFINITOconcrete(self, EstruturaFOR):
        pass

    @abstractmethod
    def visitFor_WHILEconcrete(self, EstruturaFOR):
        pass

    @abstractmethod
    def visitPrograma(self, programa):
        pass
    
    @abstractmethod
    def visitFuncao(self, funcao):
        pass

    @abstractmethod
    def visitRetornoFuncao(self, retorno):
        pass

    @abstractmethod
    def visitDeclaracaoExplicitaSimples(self, DeclaracaoExplicitaSimples):
        pass
    @abstractmethod
    def visitDeclaracaoExplicitaComposta(self, DeclaracaoExplicita):
        pass
    @abstractmethod
    def visitDeclaracaoCurta(self, DeclaracaoCurta):
        pass

    @abstractmethod
    def visitAtribuicao(self, Atribuicao):
        pass

    @abstractmethod
    def visitParametroSimples(self, Parametro):
        pass
    @abstractmethod
    def visitParametroCompostoTipoUnico(self, ParametroComposto):
        pass
    @abstractmethod
    def visitChamadaFuncao(self, ChamadaFuncao):
        pass
    @abstractmethod
    def visitEstruturaIFconcrete(self, EstruturaIF):
        pass