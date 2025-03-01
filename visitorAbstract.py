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
    def visitDeclaracaoGlobalSimples(self, declaracao):
        pass

    @abstractmethod
    def visitDeclaracaoGlobalSimplesComValor(self, declaracao):
        pass

    @abstractmethod
    def visitDeclaracaoGlobalComposta(self, declaracao):
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
    def vistAssignPlus(self, expMatRedu):
       pass

    @abstractmethod
    def vistAssignMinus(self, expMatRedu):
       pass

    @abstractmethod
    def vistAssignMult(self, expMatRedu):
       pass

    @abstractmethod
    def vistAssigndiv(self, expMatRedu):
       pass