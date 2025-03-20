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

                if(isinstance(comando,sa.Unario)):
                    print(blank(),end='')
                elif(isinstance(comando,sa.Atribuicao)):
                    print(blank(), end='')
                elif(isinstance(comando,sa.ChamadaFuncao)):
                    print(blank(),end='')

                comando.accept(self)

                if(isinstance(comando,sa.Declaracao)):
                    print('')
                elif(isinstance(comando,sa.Atribuicao)):
                    print('')
                elif(isinstance(comando,sa.ChamadaFuncao)):
                    print('')
                elif(isinstance(comando, sa.RetornoFuncao)):
                    print('')
                
    
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
        global tab
        print(blank() + 'for ', end='')
        EstruturaFOR.declaracao.accept(self)
        print('; ', end='')
        EstruturaFOR.expressao1.accept(self)
        print('; ', end='')
        EstruturaFOR.expressao2.accept(self)
        print(' {')
        tab = tab + 3
        EstruturaFOR.codigo.accept(self)
        tab = tab - 3
        print('\n' + blank() +'}')

    def visitFor_INFINITOconcrete(self, EstruturaFOR):
        global tab
        print(blank() + 'for {', end='')
        tab = tab + 3
        EstruturaFOR.codigo.accept(self)
        tab = tab - 3
        print('\n' + blank() + '}')

    def visitFor_WHILEconcrete(self, EstruturaFOR):
        global tab
        print(blank() + 'for ', end='')
        EstruturaFOR.expressao.accept(self)
        print(' {')  
        tab = tab + 3
        EstruturaFOR.codigo.accept(self)
        tab = tab - 3
        print('\n' + blank() + '}')
        
    def visitEstruturaIFconcrete(self, estruturaElse):
        global tab
        print(blank() + 'if ', end='')
        estruturaElse.expressao.accept(self)
        print(' {')
        tab = tab + 3
        estruturaElse.codigo.accept(self)
        tab = tab - 3
        print('\n' + blank() + '}')

    def visitEstruturaIF_ELSEconcrete (self, estruturaElse):
        global tab
        print(blank() +'if ', end='')
        estruturaElse.expressao.accept(self)
        print('{')
        tab = tab + 3
        estruturaElse.codigo.accept(self)
        tab = tab - 3
        print('\n'+blank()+'}')
        estruturaElse.expressao_else.accept(self)

    def visitEstruturaELSEconcrete(self, estruturaElse):
        global tab
        print(blank() + 'else ', end='')
        print('{')
        tab = tab + 3
        estruturaElse.codigo.accept(self)
        tab = tab - 3
        print('\n' + blank() + '}',end="")
        
    def visitEstruturaELSE_IFconcrete(self, estruturaElse):
        print('else ', end='')
        estruturaElse.estrutura_if.accept(self)
    
    def visitFuncao(self, funcao):
         global tab
         print('\nfunc',f'{funcao.id} (', end='')

         if(funcao.lista_parametros != None):
            funcao.lista_parametros.accept(self)

         print(')', end='')
         if(funcao.tipo_retorno != None):
             print(f' {funcao.tipo_retorno} ', end='')
         print ("{\n")
         tab = tab + 3
         funcao.codigo.accept(self)
         tab = tab - 3
         print ("\n}")

    def visitAtribuicao(self, Atribuicao):
        for _ in Atribuicao.identificadores:
            print(f'{_} ',end='')
        print('=',end=' ')
        for _ in Atribuicao.expressoes:
            _.accept(self)
    
    def visitDeclaracaoExplicitaSimples(self, DeclaracaoExplicitaSimples):
        if(DeclaracaoExplicitaSimples.valor != None):
            print(blank() + f'var {DeclaracaoExplicitaSimples.nomeVariavel} {DeclaracaoExplicitaSimples.tipo} = ',end="")
            DeclaracaoExplicitaSimples.valor.accept(self)
        else:
            print(blank() + f'var {DeclaracaoExplicitaSimples.nomeVariavel} {DeclaracaoExplicitaSimples.tipo}',end="")
    
    def visitDeclaracaoExplicitaComposta(self, DeclaracaoExplicita):
        global tab
        tab = tab + 3
        print('var (')
        for declaracao in DeclaracaoExplicita.listaVariaveis:
            declaracao.accept(self) 
            print("")
        tab = tab - 3
        print(')')

    def visitDeclaracaoExplicitaEmListaSimples(self, DeclaracaoExplicita):
        print(blank()+"var ", end='')
        for declaracao in DeclaracaoExplicita.listaVariaveis:
            print(declaracao, end=' ')
        print(DeclaracaoExplicita.tipo, end=' ')
        if(DeclaracaoExplicita.listaExpressoes != None):
            print('=', end=' ')
            for expressao in DeclaracaoExplicita.listaExpressoes:
                expressao.accept(self)
                print('', end=' ')

    def visitDeclaracaoCurta(self, DeclaracaoCurta):
        print(blank(), end='')
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

    def visitParametroCompostoVariosTipos(self, ParametroComposto):
        for _ in ParametroComposto.Parametros:
            _.accept(self)
    
    def visitChamadaFuncao(self, estrutura):
        print(estrutura.nome, end='')
        print('(',end='')
        if(estrutura.lista_parametros != None):
            for est in estrutura.lista_parametros:
                est.accept(self)
                print(" ",end = '')
        print(')',end='')

    def visitRetornoFuncao(self, retorno):
        print(blank() + 'return ', end='')
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
