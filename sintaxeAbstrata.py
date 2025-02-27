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
    def getNomeVariavel(self):
        pass

class DeclaracaoGlobalSimplesConcrete(DeclaracaoGlobalSimples):
    def __init__(self, nomeVariavel,tipo):
        self.nomeVariavel = nomeVariavel
        self.tipo = tipo
        self.valor = None

    def accept(self, visitor):
        return visitor.visitDeclaracaoGlobalSimples(self)
    
    def getNomeVariavel(self):
        return self.nomeVariavel

class DeclaracaoGlobalSimplesComValorConcrete(DeclaracaoGlobalSimples):
    def __init__(self, nomeVariavel,tipo,valor):
        self.nomeVariavel = nomeVariavel
        self.tipo = tipo
        self.valor = valor

    def accept(self, visitor):
        return visitor.visitDeclaracaoGlobalSimplesComValor(self)

    def getNomeVariavel(self):
        return self.nomeVariavel

class DeclaracaoGlobalComposta(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclaracaoGlobalCompostaConcrete(DeclaracaoGlobal):
    def __init__(self, listaVariaveis):
        self.listaVariaveis = listaVariaveis

    def accept(self, visitor):
        return visitor.visitDeclaracaoGlobalComposta(self)

class EstruturaIF(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class EstruturaIFconcrete(EstruturaIF):
    def __init__(self, expressao, codigo):
        self.expressao = expressao
        self.codigo = codigo

    def accept(self, visitor):
        return visitor.visitEstruturaIFconcrete(self)

class EstruturaIF_ELSEconcrete(EstruturaIF):
    def __init__(self, expressao, codigo, expressao_else):
        self.expressao = expressao
        self.codigo = codigo
        self.expressao_else = expressao_else
    
    def accept(self, visitor):
        return visitor.visitEstruturaIF_ELSEconcrete(self)
        

class EstruturaELSE(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class EstruturaELSEconcrete(EstruturaELSE):
    def __init__(self, codigo):
        self.codigo = codigo

    def accept(self, visitor):
        return visitor.visitEstruturaELSEconcrete(self)

class EstruturaELSE_IFconcrete(EstruturaELSE):
    def __init__(self, estrutura_if):
        self.estrutura_if = estrutura_if

    def accept(self, visitor):
        return visitor.visitEstruturaELSE_IFconcrete(self)
        

class For_CLIKE(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class For_CLIKEconcrete(For_CLIKE):
    def __init__(self, declaracao, expressao1, expressao2, codigo):
        self.declaracao = declaracao
        self.expressao1 = expressao1
        self.expressao2 = expressao2
        self.codigo = codigo

    def accept(self,visitor):
        return visitor.visitFor_CLIKEconcrete(self)

class For_INFINITO(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class For_INFINITOconcrete(For_INFINITO):
    def __init__(codigo):
        self.codigo = codigo

    def accept(self,visitor):
        return visitor.visitFor_INFINITOconcrete(self)

class For_WHILE(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class For_WHILEconcrete(For_WHILE):
    def __init__(self, expressao, codigo):
        self.expressao = codigo
        self.codigo = codigo

    def accept(self, visitor):
        return visitor.visitFor_WHILEconcrete(self)

class EstruturaFOR(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class EstruturaFOR_CLIKE(EstruturaFOR):
    def __init__(self, for_clike):
        self.for_clike = for_clike

    def accept(self, visitor):
        return visitor.visitEstruturaFOR_CLIKE(self)

class EstruturaFOR_INFINITO(EstruturaFOR):
    def __init__(self, for_infinito):
        self.for_infinito = for_infinito

    def accept(self, visitor):
        return visitor.visitEstruturaFOR_CLIKE(self)

class EstruturaFOR_WHILE(EstruturaFOR):
    def __init__(self, for_while):
        self.for_while = for_while

    def accept(self, visitor):
        return visitor.visitEstruturaFOR_CLIKE(self)
