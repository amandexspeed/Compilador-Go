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
        global nomeArquivo
        global nomePacote

        if(ts.getBindable(funcao.nome) != None):
            print("Função " + funcao.nome + " já declarada")
        else:
            params = None
            if(funcao.lista_parametros != None):
                params = funcao.lista_parametros.accept(self)
            ts.addFunction(funcao.nome, funcao.tipoRetorno, params, nomePacote , 'global' + nomeArquivo)

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