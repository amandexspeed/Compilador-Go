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
        print("Programa: ", programa.getNome())

    def visitFuncao(self, funcao):
        print("Funcao: ", funcao.getNome())

    def visitPacote(self, pacote):
        print("Pacote: ", pacote.getNome())

    def visitImportacaoSimples(self, importacao):
        print("Importacao: ", importacao.getNome())

    def visitImportacaoComposta(self, importacao):
        print("Importacao: ", importacao.getNome())

    def visitDeclaracaoGlobalSimples(self, declaracao):
        print("Declaracao: Nome da Variavel ", declaracao.nomeVariavel + " Tipo: " + declaracao.tipo)

    def visitDeclaracaoGlobalSimplesComValor(self, declaracao):
        print("Declaracao: Nome da Variavel ", declaracao.nomeVariavel + " Tipo: " + declaracao.tipo + " Valor: " + declaracao.valor)

    def visitDeclaracaoGlobalComposta(self, declaracao):
        for variavel in declaracao.listaVariaveis:
            variavel.accept(self)
    
    def visitExpressaoAND(self, expressao):
        expressao.expesq.accept(self)
        print('&&', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoOR(self, expressao):
        expressao.expesq.accept(self)
        print('||', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoIGUAL(self, expressao):
        expressao.expesq.accept(self)
        print('==', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoDIFFERENT(self, expressao):
        expressao.expesq.accept(self)
        print('!=', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoGREATER(self, expressao):
        expressao.expesq.accept(self)
        print('>', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoLESS(self, expressao):
        expressao.expesq.accept(self)
        print('<', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoGREAT_OR_EQUAL(self, expressao):
        expressao.expesq.accept(self)
        print('>=', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoLESS_OR_EQUAL(self, expressao):
        expressao.expesq.accept(self)
        print('<=', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoSOMA(self, expressao):
        expressao.expesq.accept(self)
        print('+', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoSUB(self, expressao):
        expressao.expesq.accept(self)
        print('-', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoMULT(self, expressao):
        expressao.expesq.accept(self)
        print('*', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoMOD(self, expressao):
        expressao.expesq.accept(self)
        print('%', end='')
        expressao.expdir.accept(self)
    
    def visitExpressaoDIV(self, expressao):
        expressao.expesq.accept(self)
        print('/', end='')
        expressao.expdir.accept(self)
    
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

    def vistAssignPlus(self, expMatRedu):
       print(expMatRedu.id1, end='')
       print('+=', end='')
       expMatRedu.exp.accept(self)
    
    def vistAssignMinus(self, expMatRedu):
       print(expMatRedu.id1, end='')
       print('-=', end='')
       expMatRedu.exp.accept(self)

    def vistAssignMult(self, expMatRedu):
       print(expMatRedu.id1, end='')
       print('*=', end='')
       expMatRedu.exp.accept(self)

    def vistAssigndiv(self, expMatRedu):
       print(expMatRedu.id1, end='')
       print('/=', end='')
       expMatRedu.exp.accept(self)


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
