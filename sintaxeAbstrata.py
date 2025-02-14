from abc import abstractmethod
from abc import ABCMeta

class Pacote(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    @abstractmethod
    def getNome(self):
        pass

class PacoteConcrete(Pacote):
    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def accept(self, visitor):
        return visitor.visitPacote(self)

class Importacao(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    @abstractmethod
    def getNome(self):
        pass

class ImportacaoSimplesConcrete(Importacao):
    def __init__(self, nome):
        self.nome= nome

    def accept(self, visitor):
        return visitor.visitImportacaoSimples(self)
    
    def getNome(self):
        return self.nome
    
class ImportacaoCompostaConcrete(Importacao):
    def __init__(self, nome, importacoes):
        self.nome= nome
        self.importacoes = importacoes

    def accept(self, visitor):
        return visitor.visitImportacaoComposta(self)
    
    def getNome(self):
        return self.nome + self.importacoes.toList()

class Programa(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ProgramaConcrete(Programa):
    def __init__(self, pacote, importacao, declaracaoGlobal, funcoes_codigo):
        self.pacote = pacote
        self.importacao = importacao
        self.declaracaoGlobal = declaracaoGlobal
        self.funcoes_codigo = funcoes_codigo

    def accept(self, visitor):
        return visitor.visitPrograma(self)

class Funcao(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class FuncaoConcrete(Funcao):
    def __init__(self, id, lista_parametros, tipo_retorno, codigo):
        self.id = id
        self.lista_parametros = lista_parametros
        self.tipo_retorno = tipo_retorno
        self.codigo = codigo

    def accept(self, visitor):
        return visitor.visitFuncao(self)

    
class DeclaracaoGlobal(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclaracaoGlobalSimples(DeclaracaoGlobal,metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclaracaoGlobalSimplesConcrete(DeclaracaoGlobalSimples):
    def __init__(self, nomeVariavel,tipo):
        self.nomeVariavel = nomeVariavel
        self.tipo = tipo
        self.valor = None

    def accept(self, visitor):
        return visitor.visitDeclaracaoGlobalSimples(self)

class DeclaracaoGlobalSimplesComValorConcrete(DeclaracaoGlobalSimples):
    def __init__(self, nomeVariavel,tipo,valor):
        self.nomeVariavel = nomeVariavel
        self.tipo = tipo
        self.valor = valor

    def accept(self, visitor):
        return visitor.visitDeclaracaoGlobalSimplesComValor(self)

class DeclaracaoGlobalComposta(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclaracaoGlobalCompostaConcrete(DeclaracaoGlobal):
    def _init__(self, listaVariaveis):
        self.listaVariaveis = listaVariaveis

    def accept(self, visitor):
        return visitor.visitDeclaracaoGlobalComposta(self)