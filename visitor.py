from visitorAbstract import AbstractVisitor
from analiseSintatica import *

tab = 0

def blank():
    p=''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):

    def visitPacote(self, pacote):
        print("Pacote: ", pacote.getNome())
        pacote.nome.accept(self)

    def visitImportacaoSimples(self, importacao):
        print("Importacao: ", importacao.getNome())
        importacao.nome.accept(self)

    def visitImportacaoComposta(self, importacao):
        print("Importacao: ", importacao.getNome())
        importacao.nome.accept(self)
        importacao.importacoes.accept(self)

    def visitDeclaracaoGlobalSimples(self, declaracao):
        print("Declaracao: Nome da Variavel ", declaracao.nomeVariavel + " Tipo: " + declaracao.tipo)
        declaracao.nome.accept(self)
        declaracao.tipo.accept(self)

    def visitDeclaracaoGlobalSimplesComValor(self, declaracao):
        print("Declaracao: Nome da Variavel ", declaracao.nomeVariavel + " Tipo: " + declaracao.tipo + " Valor: " + declaracao.valor)
        declaracao.nome.accept(self)
        declaracao.tipo.accept(self)
        declaracao.valor.accept(self)

    def visitDeclaracaoGlobalComposta(self, declaracao):
        for variavel in declaracao.listaVariaveis:
            variavel.accept(self)


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