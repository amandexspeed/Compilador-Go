from visitor import *
import tabelaSimbolos as ts

global isFineSemantic

class AnaliseSemantica(AbstractVisitor):

    def __init__(self, nomeArquivo):
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
        scope = ts.currentScope()
        if(scope[ts.TYPE] != retorno.expressao.accept(self)):
            print("Erro: Tipo de retorno incompatível")
            global isFineSemantic
            isFineSemantic = False
            return None
        return scope[ts.TYPE]

    def visitAtribuicao(self, Atribuicao):
        if(ts.getBindable(Atribuicao.identificador) == None):
            print("Erro: Variável não declarada")
            global isFineSemantic
            isFineSemantic = False
        else:
            tipo = Atribuicao.expressao.accept(self)
            if(ts.getBindable(Atribuicao.identificador)[ts.TYPE] != tipo):
                print("Erro: Tipo de variável não compatível com o valor atribuído")
                global isFineSemantic
                isFineSemantic = False

    def visitDeclaracaoExplicitaSimples(self, DeclaracaoExplicitaSimples):
        if(ts.getBindable(DeclaracaoExplicitaSimples.nome) != None):
            print("Aviso: Variável redeclarada")
        if(DeclaracaoExplicitaSimples.valor != None):
            if(DeclaracaoExplicitaSimples.tipo != DeclaracaoExplicitaSimples.valor.visit(self)):              
                print("Erro: Tipo de variável não compatível com o valor atribuído")
                global isFineSemantic
                isFineSemantic = False
            else:
                ts.addExplicitVariable(DeclaracaoExplicitaSimples.nome, DeclaracaoExplicitaSimples.tipo)
                return DeclaracaoExplicitaSimples.tipo


    def visitDeclaracaoExplicitaEmListaSimples(self, DeclaracaoExplicita):
        listaObjetosDeclarados = []
        for variavel in DeclaracaoExplicita.listaVariaveis:
            listaObjetosDeclarados.append(sa.DeclaracaoExplicitaSimplesConcrete(variavel, DeclaracaoExplicita.tipo, None))

        if(DeclaracaoExplicita.listaExpressoes != None):
            if(len(DeclaracaoExplicita.listaVariaveis) != len(DeclaracaoExplicita.listaExpressoes)):
                print("Erro: Número de variáveis e valores incompatíveis")
                global isFineSemantic
                isFineSemantic = False
            
            for i in range(len(listaObjetosDeclarados)):
                listaObjetosDeclarados[i].valor = DeclaracaoExplicita.listaExpressoes[i]

        for declaracao in listaObjetosDeclarados:
            declaracao.accept(self)

    def visitDeclaracaoExplicitaComposta(self, DeclaracaoExplicita):
        for variavel in DeclaracaoExplicita.listaVariaveis:
            variavel.accept(self)

    def visitDeclaracaoCurta(self, DeclaracaoCurta):
        if(ts.getBindable(DeclaracaoCurta.nome) != None):
            print("Aviso: Variável redeclarada")

        if(len(DeclaracaoCurta.expressao) != len(DeclaracaoCurta.identificadores)):
            print("Erro: Número de variáveis e valores incompatíveis")
            global isFineSemantic
            isFineSemantic = False

        for i in range(len(DeclaracaoCurta.identificadores)):
            tipo = DeclaracaoCurta.expressoes[i].accept(self)
            ts.addMultableVariable(DeclaracaoCurta.nome, tipo)

    def visitParametroSimples(self, Parametro):
        pass

    def visitParametroCompostoTipoUnico(self, ParametroComposto):
        pass

    def visitParametroCompostoVariosTipos(self, ParametroComposto):
        pass

    def visitChamadaFuncao(self, ChamadaFuncao):
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