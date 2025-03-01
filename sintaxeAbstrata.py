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
    def __init__(self, pacote, importacao, declaracaoExplicita, funcoes_codigo):
        self.pacote = pacote
        self.importacao = importacao
        self.declaracaoExplicita = declaracaoExplicita
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

class Atribuicao(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class AtribuicaoConcrete(Atribuicao):
    def __init__(self, identificadores, expressoes):
        self.identificadores = identificadores
        self.expressoes = expressoes

    def accept(self, visitor):
        return visitor.visitAtribuicao(self)
    
class Declaracao(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class DeclaracaoExplicita(Declaracao,metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclaracaoExplicitaSimples(DeclaracaoExplicita,metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    def getNomeVariavel(self):
        pass

class DeclaracaoExplicitaSimplesConcrete(DeclaracaoExplicitaSimples):

    def __init__(self, nomeVariavel, tipo, valor):
        self.nomeVariavel = nomeVariavel
        self.tipo = tipo
        self.valor = valor

    def accept(self, visitor):
        return visitor.visitDeclaracaoExplicitaSimples(self)
    
    def getNomeVariavel(self):
        return self.nomeVariavel

class DeclaracaoExplicitaComposta(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclaracaoExplicitaCompostaConcrete(DeclaracaoExplicita):
    def __init__(self, listaVariaveis):
        self.listaVariaveis = listaVariaveis

    def accept(self, visitor):
        return visitor.visitDeclaracaoExplicitaComposta(self)

class DeclaracaoCurta(Declaracao,metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclaracaoCurtaConcrete(DeclaracaoCurta):
    def __init__(self, identificadores, expressoes):
        self.identificadores = identificadores
        self.expressoes = expressoes

    def accept(self, visitor):
        return visitor.visitDeclaracaoCurta(self)    
    
class Parametro(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ParametroSimplesConcrete(Parametro):
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
    
    def accept(self, visitor):
        return visitor.visitParametroSimples(self)
    
class ParametroComposto(Parametro,metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    @abstractmethod
    def adicionarIdentificador(self, identificador):
        pass

class ParametroCompostoTipoUnicoConcrete(ParametroComposto):
    def __init__(self, identificadores, tipo):
        self.identificadores = identificadores
        self.tipo = tipo

    def accept(self, visitor):
        return visitor.visitParametroCompostoTipoUnico(self)

    def adicionarIdentificador(self, identificador):
        self.identificadores + [identificador]

class ParametroCompostoVariosTiposConcrete(ParametroComposto):
    def __init__(self, identificadores):
        self.identificadores = identificadores

    def accept(self, visitor):
        return visitor.visitParametroCompostoTipoVazio(self)
    
    def adicionarIdentificador(self, identificador):
        self.identificadores + [identificador]

class ChamadaFuncao(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ChamadaFuncaoConcrete(ChamadaFuncao):
    def __init__(self, nome, lista_parametros):
        self.nome = nome
        self.lista_parametros = lista_parametros

    def accept(self, visitor):
        return visitor.visitChamadaFuncao(self)

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
        
class EstruturaFOR(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class For_CLIKEconcrete(EstruturaFOR):
    def __init__(self, declaracao, expressao1, expressao2, codigo):
        self.declaracao = declaracao
        self.expressao1 = expressao1
        self.expressao2 = expressao2
        self.codigo = codigo

    def accept(self,visitor):
        return visitor.visitFor_CLIKEconcrete(self)

class For_INFINITO(EstruturaFOR):
    @abstractmethod
    def accept(self, visitor):
        pass

class For_INFINITOconcrete(For_INFINITO):
    def __init__(self,codigo):
        self.codigo = codigo

    def accept(self,visitor):
        return visitor.visitFor_INFINITOconcrete(self)

class For_WHILEconcrete(EstruturaFOR):
    def __init__(self, expressao, codigo):
        self.expressao = expressao
        self.codigo = codigo

    def accept(self, visitor):
        return visitor.visitFor_WHILEconcrete(self)

class Expressao(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpressaoAND(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoAND(self)

class ExpressaoOR(Expressao):
    def __init__(self,esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoOR(self)

class ExpressoaIGUAL(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    
    def accept(self, visitor):
        return visitor.visitExpressaoIGUAL(self)
    
class ExpressaoDIFFERENT(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoDIFFERENT(self)

class ExpressaoGREATER (Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    
    def accept(self, visitor):
        return visitor.visitExpressaoGREATER(self)

class ExpressaoLESS (Expressao):
    def __init__ (self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    
    def accept(self, visitor):
        return visitor.visitExpressaoLESS(self)

class ExpressaoGREAT_OR_EQUAL(Expressao):
    def __init__ (self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoGREAT_OR_EQUAL(self)
    
class ExpressaoLESS_OR_EQUAL(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    
    def accept(self, visitor):
        return visitor.visitExpressaoLESS_OR_EQUAL(self)
    
class ExpressaoSOMA(Expressao):
    def __init__(self,esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    
    def accept (self, visitor):
        return visitor.visitExpressaoSOMA(self)

class ExpressaoSUB(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    
    def accept(self, visitor):
        return visitor.visitExpressaoSUB(self)
    
class ExpressaoMULT(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    
    def accept(self, visitor):
        return visitor.visitExpressaoMULT(self)
    
class ExpressaoMOD(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoMOD(self)
    
class ExpressaoDIV(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    
    def accept(self, visitor):
        return visitor.visitExpressaoDIV(self)
    
class ExpressaoNEGATION(Expressao):
    def __init__(self, operando):
        self.operando = operando
        
    def accept(self, visitor):
        return visitor.visitExpressaoNEGATION(self)

class Unario (Expressao):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpressaoINCREMENTO(Unario):
    def __init__(self, id):
        self.id = id
        
    def accept(self, visitor):
        return visitor.visitExpressaoINCREMENTO(self)

class ExpressaoPRE_INCREMENTO(Unario):
    def __init__(self,id):
        self.id = id
       
    def accept(self, visitor):
        return visitor.visitExpressaoPRE_INCREMENTO(self)

class ExpressaoDECREMENTO(Unario):
    def __init__(self,id):
        self.id = id
    
    def accept(self, visitor):
        return visitor.visitExpressaoDECREMENTO(self)

class ExpressaoPRE_DECREMENTO(Unario):
    def __init__(self,id):
        self.id = id
    
    def accept(self, visitor):
        return visitor.visitExpressaoPRE_DECREMENTO(self)

class Constante (Expressao):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConstanteConcreto(Constante):
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo
    def accept(self, visitor):
        return visitor.visitConstanteConcreto(self)

class ExpressaoPARENTESE(Expressao):
    def __init__(self, expressao):
        self.expressao = expressao
    
    def accept(self, visitor):
        return visitor.visitExpressaoPARENTESE(self)

#Para a parte de expressões matemáticas reduzidas

class expMatRedu():
    @abstractmethod
    def accept(self, visitor):
        pass

class assignPlus():
    def __init__(self, id1, exp):
       self.id1 = id1
       self.exp = exp

class assignMinus():
    def __init__(self, id1, exp):
       self.id1 = id1
       self.exp = exp

class assignMult():
    def __init__(self, id1, exp):
       self.id1 = id1
       self.exp = exp

class assignDiv():
    def __init__(self, id1, exp):
       self.id1 = id1
       self.exp = exp