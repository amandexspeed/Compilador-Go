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

    #Começando a parte de expressões...
    @abstractmethod
    def vistAnd(self, e):
        pass

    @abstractmethod
    def visitOr(self, ou):
        pass
    
    @abstractmethod
    def visitEquals(self, igual):
        pass

    @abstractmethod
    def visitDiferent(self, diferente):
        pass

    @abstractmethod
    def visitMaiorQue(self, maior):
        pass

    @abstractmethod
    def visitMenor(self,menor):
        pass

    @abstractmethod
    def visitMenorIgual(self,menorIgual):
        pass

    @abstractmethod
    def visitMaiorIgual(self, maiorIgual):
        pass

    @abstractmethod
    def visitSoma(self, soma):
        pass

    @abstractmethod
    def visitSub(self, sub):
        pass

    @abstractmethod
    def visiMult(self, mult):
        pass

    @abstractmethod
    def visitDiv(self, div):
        pass

    @abstractmethod
    def visitMod(self, mod):
        pass

    #Como fazer para o unário????