from abc import ABCMeta, abstractmethod

class abstratVisitor(metaclass = ABCMeta):

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
   