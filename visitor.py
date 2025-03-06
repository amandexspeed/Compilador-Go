from visitorAbstract import AbstractVisitor
from analiseSintatica import *

tab = 0
 
def blank():
    p=''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):
    
    def visitPrograma(self, programa):
        programa.pacote.accept(self)
        if(programa.importacao != None):
            programa.importacao.accept(self)
        if(programa.declaracaoExplicita != None ):
            programa.declaracaoExplicita.accept(self)
        if(programa.funcoes_codigo != None):
            programa.funcoes_codigo.accept(self)

    def visitPacote(self, pacote):
        print("package ", pacote.getNome())

    def visitImportacaoSimples(self, importacao):
        print("import ", importacao.nome)

    def visitImportacaoComposta(self, importacao):
        print("import ", importacao.nome)
        for importacaoSimples in importacao.importacoes:
            importacaoSimples.accept(self)

    def visitCodigo(self, codigo):
        if(codigo.listaEstruturas != None):
            for comando in codigo.listaEstruturas:
                comando.accept(self)
    
    def visitExpressaoAND(self, expressao):
        expressao.esquerda.accept(self)
        print('&&', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoOR(self, expressao):
        expressao.esquerda.accept(self)
        print('||', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoIGUAL(self, expressao):
        expressao.esquerda.accept(self)
        print('==', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoDIFFERENT(self, expressao):
        expressao.esquerda.accept(self)
        print('!=', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoGREATER(self, expressao):
        expressao.esquerda.accept(self)
        print('>', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoLESS(self, expressao):
        expressao.esquerda.accept(self)
        print('<', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoGREAT_OR_EQUAL(self, expressao):
        expressao.esquerda.accept(self)
        print('>=', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoLESS_OR_EQUAL(self, expressao):
        expressao.esquerda.accept(self)
        print('<=', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoSOMA(self, expressao):
        expressao.esquerda.accept(self)
        print('+', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoSUB(self, expressao):
        expressao.esquerda.accept(self)
        print('-', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoMULT(self, expressao):
        expressao.esquerda.accept(self)
        print('*', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoMOD(self, expressao):
        expressao.esquerda.accept(self)
        print('%', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoDIV(self, expressao):
        expressao.esquerda.accept(self)
        print('/', end='')
        expressao.direita.accept(self)
    
    def visitExpressaoNEGATION(self, expressao):
        print('!', end='')
        expressao.operando.accept(self)
    
    def visitExpressaoINCREMENTO(self, expressao):
        print(f'{expressao.id}++', end='')
    
    def visitExpressaoPRE_INCREMENTO(self, unario):
        print(f'++{unario.id}', end='')
    
    def visitExpressaoDECREMENTO(self, unario):
        print(f'{unario.id}--', end='')
    
    def visitExpressaoPRE_DECREMENTO(self, unario):
        print(f'--{unario.id}', end='')
    
    def visitConstanteConcreto(self, constante):
        print(constante.valor, end='')
    
    def visitExpressaoPARENTESE(self, expressao):
        print('(', end='')
        expressao.expressao.accept(self)
        print(')', end='')

    def visitAssignPlus(self, expMatRedu):
       print(expMatRedu.id1, end='')
       print('+=', end='')
       expMatRedu.exp.accept(self)
    
    def visitAssignMinus(self, expMatRedu):
       print(expMatRedu.id1, end='')
       print('-=', end='')
       expMatRedu.exp.accept(self)

    def visitAssignMult(self, expMatRedu):
       print(expMatRedu.id1, end='')
       print('*=', end='')
       expMatRedu.exp.accept(self)

    def visitAssigndiv(self, expMatRedu):
       print(expMatRedu.id1, end='')
       print('/=', end='')
       expMatRedu.exp.accept(self)

    def visitFor_CLIKEconcrete(self, EstruturaFOR):
        print('for', end='')
        EstruturaFOR.declaracao.accept(self)
        print(';', end='')
        EstruturaFOR.expressao1.accept(self)
        print(';', end='')
        EstruturaFOR.expressao2.accept(self)
        print('{')
        EstruturaFOR.codigo.accept(self)
        print('}')

    def visitFor_INFINITOconcrete(self, EstruturaFOR):
        print('for {', end='')
        EstruturaFOR.codigo.accept(self)
        print('}')

    def visitFor_WHILEconcrete(self, EstruturaFOR):
        print('for', end='')
        EstruturaFOR.expressao.accept(self)
        print('{', end='')  
        EstruturaFOR.codigo.accept(self)
        print('}')
        
    def visitEstruturaIFconcrete(self, estruturaElse):
        print('if', end='')
        estruturaElse.expressao.accept(self)
        print('{')
        estruturaElse.codigo.accept(self)
        print('}')

    def visitEstruturaIF_ELSEconcrete (self, estruturaElse):
        print('if', end='')
        estruturaElse.expressao.accept(self)
        print('{')
        estruturaElse.codigo.accept(self)
        print('}')
        estruturaElse.expressao_else.accept(self)

    def visitEstruturaELSEconcrete(self, estruturaElse):
        print('else', end='')
        print('{')
        estruturaElse.codigo.accept(self)
        print('}')
        
    def visitEstruturaELSE_IFconcrete(self, estruturaElse):
        print('else', end='')
        estruturaElse.estrutura_if.accept(self)
    
    def visitFuncao(self, funcao):
         print(f'{funcao.id} (', end='')

         if(funcao.lista_parametros != None):
            funcao.lista_parametros.accept(self)

         print(')', end='')
         if(funcao.tipo_retorno != None):
             print(f' {funcao.tipo_retorno} ', end='')
         print ("{")
         funcao.codigo.accept(self)
         print ("\n}")

    def visitAtribuicao(self, Atribuicao):
        for _ in Atribuicao.identificadores:
            print(f'{_}',end='')
        print(':=',end=' ')
        for _ in Atribuicao.expressoes:
            _.accept(self)
        print('')
    
    def visitDeclaracaoExplicitaSimples(self, DeclaracaoExplicitaSimples):
        if(DeclaracaoExplicitaSimples.valor != None):
            print(f'{DeclaracaoExplicitaSimples.nomeVariavel} {DeclaracaoExplicitaSimples.tipo} := {DeclaracaoExplicitaSimples.valor}')
        else:
            print(f'{DeclaracaoExplicitaSimples.nomeVariavel} {DeclaracaoExplicitaSimples.tipo}')
    
    def visitDeclaracaoExplicitaComposta(self, DeclaracaoExplicita):
        print('var (')
        for declaracao in DeclaracaoExplicita.listaVariaveis:
            declaracao.accept(self) 
        print(')')

    def visitDeclaracaoCurta(self, DeclaracaoCurta):
        for _ in DeclaracaoCurta.identificadores:
            print(f'{_}',end=' ')
        print(':=',end=' ')
        for _ in DeclaracaoCurta.expressoes:
            _.accept(self)
            print('',end=' ')
    
    def visitParametroSimples(self, Parametro):
        print(f'{Parametro.nome} {Parametro.tipo}',end='')
    
    def visitParametroCompostoTipoUnico(self, ParametroComposto):
        print('Identificadores: ')
        for _ in ParametroComposto.identificadores:
            print(f'{_} ',end="")
        print(f'{ParametroComposto.tipo}')

    
    def visitChamadaFuncao(self, estrutura):
        print(estrutura.nome, end='')
        print('(',end='')
        if(estrutura.lista_parametros != None):
            for est in estrutura.lista_parametros:
                est.accept(self)
                print(" ",end = '')
        print(')',end='')

    def visitRetornoFuncao(self, retorno):
        print('return ', end='')
        retorno.expressao.accept(self)
   
def main():
    for arquivo in arquivos_go:
        print("-----------Visitor no arquivo: ", arquivo,"-----------")
        f = open(arquivo, "r")

        lexer.input(f.read())
        parser = yacc.yacc(start='programa')
        result = parser.parse(debug=False)
        visitor = Visitor()
        result.accept(visitor)

if __name__ == "__main__":
    main()
