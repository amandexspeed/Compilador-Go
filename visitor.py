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