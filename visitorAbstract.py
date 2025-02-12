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

   