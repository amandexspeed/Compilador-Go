from visitor import *
import tabelaSimbolos as ts

global isFineSemantic

class AnaliseSemantica(AbstractVisitor):

    def __init__(self, nomeArquivo):
        self.printer = Visitor()
        ts.beginScope('global' + nomeArquivo)

    def constCoercion(self,Exp1, Exp2):

        """Função que verifica se é possível fazer a coerção de tipos de constantes
           
           Retornos possíveis:
           
           -1: Não é possível fazer coerção - Erro de tipo
           None: Não são constantes
           ts.INT: Coerção padrão para inteiro
           ts.FLOAT64: Coerção padrão para float"""

        """Nenhuma das expressões é constante"""
        if(not(Exp1.__class__ == "ConstanteConcreto" and Exp2.__class__ == "ConstanteConcreto")):
            return None

        """Ambas as expressões são constantes"""
        if(Exp1.__class__ == "ConstanteConcreto" and Exp2.__class__ == "ConstanteConcreto"):
            
            """Se as duas tiverem mesma flag de tipo"""
            if(Exp1.tipo == Exp2.tipo):

                match Exp1.tipo: 
                    case "int": return ts.INT,
                    case "float": return ts.FLOAT64,
                    case "boolean": return ts.BOOL,
                    case "string": return ts.STRING
                    case "ID": 
                        tipoVar1 = ts.getBindable(Exp1.valor)[ts.TYPE]
                        tipoVar2 = ts.getBindable(Exp2.valor)[ts.TYPE]
                        if(tipoVar1 == tipoVar2):
                            return tipoVar1
                        else:
                            return -1
                               
            elif(Exp1.tipo == "ID"):
                '''Se as duas tiverem flag de tipo diferente, mas uma delas for ID tem que tentar coerção. 
                   Começamos por Exp 1'''
                tipoVar1 = ts.getBindable(Exp1.valor)[ts.TYPE]
                match Exp2.tipo:
                    case "int": 
                        if(tipoVar1 in ts.inteiro):
                            return tipoVar1
                        else:
                            return -1
                    
                    case "float": 
                        if(tipoVar1 in ts.real):
                            return tipoVar1
                        else:
                            return -1
                    
                    case "boolean": 
                        if(tipoVar1 == ts.BOOL):
                            return tipoVar1
                        else:
                            return -1
                    
                    case "string" : 
                        if(tipoVar1 == ts.STRING):
                            return tipoVar1
                        else:
                            return -1
                    
                    case _: return -1

            elif(Exp2.tipo == "ID"):
                '''Caso Exp2 seja ID'''
                tipoVar2 = ts.getBindable(Exp2.valor)[ts.TYPE]
                match Exp1.tipo:
                    case "int":
                        if(tipoVar2 in ts.inteiro):
                            return tipoVar2
                        else:
                            return -1
                    
                    case "float":
                        if(tipoVar2 in ts.real):
                            return tipoVar2
                        else:
                            return -1
                    
                    case "boolean":
                        if(tipoVar2 == ts.BOOL):
                            return tipoVar2
                        else:
                            return -1
                    
                    case "string" :
                        if(tipoVar2 == ts.STRING):
                            return tipoVar2
                        else:
                            return -1
                    
                    case _: return -1
            else:
                '''Aqui realmente as duas constantes são de tipos diferentes'''
                return -1
            
        '''Uma das expressões não é constante, começamos analizando Exp 1'''
        if(Exp1.__class__ == "ConstanteConcreto"):
            
            match Exp1.tipo:
                case "int":
                    tipoExp2 = Exp2.accept(self)
                    if(tipoExp2 in ts.inteiro):
                        return tipoExp2
                    else:
                        return -1
                
                case "float":
                    tipoExp2 = Exp2.accept(self)
                    if(tipoExp2 in ts.real):
                        return tipoExp2
                    else:
                        return -1
                    
                case "boolean":
                    if(Exp2.accept(self) == ts.BOOL):
                        return ts.BOOL
                    else:
                        return -1
                
                case "string":
                    if(Exp2.accept(self) == ts.STRING):
                        return ts.STRING
                    else:
                        return -1
                    
                case "ID":
                    tipoVar = ts.getBindable(Exp1.valor)[ts.TYPE]
                    if(tipoVar == Exp2.accept(self)):
                        return tipoVar
                    else:
                        return -1
                    
        '''Caso Exp2 é constante'''    
        if(Exp2.__class__ == "ConstanteConcreto"):

            match Exp2.tipo:
                case "int":
                    tipoExp1 = Exp1.accept(self)
                    if(tipoExp1 in ts.inteiro):
                        return tipoExp1
                    else:
                        return -1

                case "float":
                    tipoExp1 = Exp1.accept(self)
                    if(tipoExp1 in ts.real):
                        return tipoExp1
                    else:
                        return -1

                case "boolean":
                    if(Exp1.accept(self) == ts.BOOL):
                        return ts.BOOL
                    else:
                        return -1

                case "string":
                    if(Exp1.accept(self) == ts.STRING):
                        return ts.STRING
                    else:
                        return -1


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
        for estrutura in codigo.listaEstruturas:
            estrutura.accept(self)

    def visitExpressaoAND(self, expressao):
        """avalia a expressoa logica de AND entre operadores"""
        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoAND(expressao)

        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if (left==ts.BOOLEAN) and (right==ts.BOOLEAN):
                return ts.BOOLEAN
            else:
                print(f'ERROR semantico: necessario boleanos, mas foi encontrado {left} e {right}')
                global isFineSemantic
                isFineSemantic = False
                self.printer.visitExpressaoAND(expressao)
        
        else:
            if(coersao == ts.BOOL):
                return ts.BOOL
            print(f'ERROR semantico: necessario boleanos, encontrado {coersao}')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoAND(expressao)
        

    def visitExpressaoOR(self, expressao):
        """"avalia a expressao logica OR entre operadores"""
        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoOR(expressao)

        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right==ts.BOOL) or (left==ts.BOOL):
                return ts.BOOL 
            else:
                print(f'ERROR semantico: necessario boleanos, mas foi encontrado {left} e  {right}')
                global isFineSemantic
                isFineSemantic = False
                self.printer.visitExpressaoOR(expressao)

        else:
            if(coersao == ts.BOOL):
                return ts.BOOL
            print(f'ERROR semantico: necessario boleanos, encontrado {coersao}')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoOR(expressao)
    
    def visitExpressaoIGUAL(self, expressao):
        """"avalia a expressao logica IGUAL entre operadores"""
        coersao = self.constCoercion(expressao.esq, expressao.dir)

        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoIgual(expressao)

        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right==left):
                return ts.BOOL
            else:
                print(f'ERROR semantico: Foi encontrado tipos diferentes: {left} e  {right}')
                global isFineSemantic
                isFineSemantic = False
                self.printer.visitExpressaoIGUAL(expressao)

        else:
            return coersao
    
    def visitExpressaoDIFFERENT(self, expressao):
        """"avalia a expressao logica DIFERENTE entre operadores"""

        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoDIFFERENT(expressao)

        elif(coersao == None):

            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right==left):
                return ts.BOOL 
            else:
                print(f'ERROR semantico: É necessário tipos iguais. Foi encontrado {left} e  {right}')
                global isFineSemantic
                isFineSemantic = False
                self.printer.visitExpressaoDIFFERENT(expressao)

        else:
            return ts.BOOL
    
    def visitExpressaoGREATER(self, expressao):

        """"avalia a expressao logica MAIOR OU IGUAL entre operadores"""

        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoGREATER(expressao)

        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right in ts.Numero) and (left in ts.Numero):
                if(right==left):
                    return ts.BOOL
                else:
                    print(f'ERROR semantico: necessário tipos numéricos iguais, mas foi encontrado {left} e  {right}')
                    global isFineSemantic
                    isFineSemantic = False
                    self.printer.visitExpressaoGREATER(expressao)
            else:
                print(f'ERROR semantico: necessário tipos numéricos, mas foi encontrado {left} e  {right}')
                global isFineSemantic
                isFineSemantic = False
                self.printer.visitExpressaoGREATER(expressao)

        else:
            if(coersao in ts.Numero):
                return ts.BOOL
            print(f'ERROR semantico: necessario números, encontrado {coersao}')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoGREATER(expressao)
    
    def visitExpressaoLESS(self, expressao):

        """Avalia a expressão menor que entre operadores"""
        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoLESS(expressao)

        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right in ts.Numero) and (left in ts.Numero):
                if(right==left):
                    return ts.BOOL
                else:
                    print(f'ERROR semantico: necessário tipos numéricos iguais, mas foi encontrado {left} e  {right}')
                    global isFineSemantic
                    isFineSemantic = False
                    self.printer.visitExpressaoLESS(expressao)
            else:
                print(f'ERROR semantico: necessário tipos numéricos, mas foi encontrado {left} e  {right}')
                global isFineSemantic
                isFineSemantic = False
                self.printer.visitExpressaoLESS(expressao)

        else:
            if(coersao in ts.Numero):
                return ts.BOOL
            print(f'ERROR semantico: necessario tipo númerico, encontrado {coersao}')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoLESS(expressao)
    

    def visitExpressaoGREAT_OR_EQUAL(self, expressao):
        """Avalia a expressão maior ou igual entre operadores"""
        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoGREAT_OR_EQUAL(expressao)

        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right in ts.Numero) and (left in ts.Numero):
                if(right == left):
                    return ts.BOOL
                global isFineSemantic
                isFineSemantic = False
                print(f'ERROR semantico: necessário tipos numéricos iguais, mas foi encontrado {left} e  {right}')
                self.printer.visitExpressaoGREAT_OR_EQUAL(expressao)
            else:
                print(f'ERROR semantico: necessário tipos numéricos iguais, mas foi encontrado {left} e  {right}')
                global isFineSemantic
                isFineSemantic = False
                self.printer.visitExpressaoGREAT_OR_EQUAL(expressao)
        else:
            if(coersao == ts.BOOL):
                return ts.BOOL
            print(f'ERROR semantico: necessario tipo númerico, encontrado {coersao}')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoGREAT_OR_EQUAL(expressao)

    def visitExpressaoLESS_OR_EQUAL(self, expressao):
        """Avalia a expressão menor ou igual que entre operadroes"""
        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoLESS_OR_EQUAL(expressao)
        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right in ts.Numero) and (left in ts.Numero):
                if(right==left):
                    return ts.BOOL
                else:
                    print(f'ERROR semantico: necessario numeros do mesmo tipo {left} e  {right}')
                    self.isFineSemantic = False
                    self.printer.visitExpressaoLESS_OR_EQUAL(expressao)
            else:
                print(f'ERROR semantico: necessario numeros do mesmo tipo {type(left)} e  {type(right)}')
                self.isFineSemantic = False
                self.printer.visitExpressaoLESS_OR_EQUAL(expressao)
        else:
            if(coersao in ts.Numero):
                return ts.BOOL
            print(f'ERROR semantico: necessario tipo númerico, encontrado {coersao}')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoLESS_OR_EQUAL(expressao)
    
    def visitExpressaoSOMA(self, expressao):
        """Avalia a expressao de soma entre operadroes"""
        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoSOMA(expressao)
        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right in ts.Numero) and (left in ts.Numero):
                if(right==left):
                    return right
                else:
                    print(f'ERROR semantico: necessario numeros do mesmo tipo {left} e  {right}')
                    self.isFineSemantic = False
                    self.printer.visitExpressaoSOMA(expressao)
            else:
                print(f'ERROR semantico: necessario numeros do mesmo tipo {type(left)} e  {type(right)}')
                self.isFineSemantic = False
                self.printer.visitExpressaoSOMA(expressao)
        else:
            if(coersao in ts.Numero):
                return coersao
            print(f'ERROR semantico: necessario tipo númerico, encontrado {coersao}')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoSOMA(expressao)
    
    def visitExpressaoSUB(self, expressao):
        """Avalia a expressao de subtracao entre operadroes"""
        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoSUB(expressao)
        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right in ts.Numero) and (left in ts.Numero):
                if(right == left):
                    return right
                else:
                    print(f'ERROR semantico: esperado numeros do mesmo tipo mas recebeu {left} e  {right}')
                    self.isFineSemantic = False
                    self.printer.visitExpressaoSUB(expressao)
            else:
                print(f'ERROR semantico: esperado tipos numericos mas recebeu {left} e  {right}')
                self.isFineSemantic = False
                self.printer.visitExpressaoSUB(expressao)
        else:
            if(coersao in ts.Numero):
                return coersao
            print(f'ERROR semantico: necessario tipo númerico, encontrado {coersao}')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoSUB(expressao)

    def visitExpressaoMULT(self, expressao):
        """Avalia se a multiplicação é válida"""
        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoMULT(expressao)
        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right in ts.Numero) and (left in ts.Numero):
                if(right == left):
                    return right
                else:
                    print(f'ERROR semantico: necessario numeros do mesmo tipo {left} e  {right}')
                    self.isFineSemantic = False
                    self.printer.visitExpressaoMULT(expressao)
            else:
                if(coersao in ts.Numero):
                    return coersao
                print(f'ERROR semantico: necessario numero,encontrado {coersao}')
                self.isFineSemantic = False
                self.printer.visitExpressaoMULT(expressao)
            
    def visitExpressaoMOD(self, expressao):
        """Avalia a expressao de modulo entre operadroes"""
        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoMOD(expressao)
        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right in ts.Numero) and (left in ts.Numero):
                if(right == left):
                    return ts.INT
                else:
                    print(f'ERROR semantico: esperado numeros do mesmo tipo mas recebeu {left} e  {right}')
                    self.isFineSemantic = False
                    self.printer.visitExpressaoMOD(expressao)
            else:
                print(f'ERROR semantico: esperado tipos numerios mas recebeu {left} e  {right}')
                self.isFineSemantic = False
                self.printer.visitExpressaoMOD(expressao)
        else:
            if(coersao in ts.Numero):
                return ts.INT
        
    def visitExpressaoDIV(self, expressao):
        """Avalia a expressao de divisao entre operadroes"""
        coersao = self.constCoercion(expressao.esq, expressao.dir)
        if(coersao == -1):
            print(f'ERROR semantico: As constantes são de tipos diferentes')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoDIV(expressao)
        elif(coersao == None):
            left = expressao.esq.accept(self)
            right = expressao.dir.accept(self)
            global isFineSemantic
            if(right in ts.Numero) and (left in ts.Numero):
                if(right == left):
                    return right
                else:
                    print(f'ERROR semantico: esperado numeros do mesmo tipo mas recebeu {left} e  {right}')
                    self.isFineSemantic = False
                    self.printer.visitExpressaoDIV(expressao)
            else:
                print(f'ERROR semantico: esperado tipos numericos mas recebeu {left} e  {right}')
                self.isFineSemantic = False
                self.printer.visitExpressaoDIV(expressao)
        else:
            if(coersao in ts.Numero):
                return coersao
            print(f'ERROR semantico: necessario tipo númerico, encontrado {coersao}')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitExpressaoDIV(expressao)

    def visitExpressaoNEGATION(self, expressao):
        """Avalia a expressao de negacao"""
        exp = expressao.operando.accept(self)
        global isFineSemantic
        if(exp in ts.BOOL):
            return ts.BOOL
        else:
            print(f'ERROR semantico: esperado tipo boleano mas recebeu {exp}')
            self.isFineSemantic = False
            self.printer.visitExpressaoNEGATION(expressao)
        
    def visitExpressaoINCREMENTO(self, expressao):
        tipoId = ts.getBindable(expressao.id)[ts.TYPE]
        if(tipoId != ts.Numero):
           print(f'ERROR semantico: Variavel {expressao.id} deve ser do tipo numerico')
           global isFineSemantic
           isFineSemantic = False
           self.printer.visitExpressaoINCREMENTO(expressao)

    
    def visitExpressaoPRE_INCREMENTO(self, expressao):
        tipoId = ts.getBindable(expressao.id)[ts.TYPE]
        if(tipoId != ts.Numero):
           print(f'ERROR semantico: Variavel {expressao.id} deve ser do tipo numerico')
           global isFineSemantic
           isFineSemantic = False
           self.printer.visitExpressaoPRE_INCREMENTO(expressao)
    
    def visitExpressaoDECREMENTO(self, expressao):
        tipoId = ts.getBindable(expressao.id)[ts.TYPE]
        if(tipoId != ts.Numero):
           print(f'ERROR semantico: Variavel {expressao.id} deve ser do tipo numerico')
           global isFineSemantic
           isFineSemantic = False
           self.printer.visitExpressaoDECREMENTO(expressao)
   
    def visitExpressaoPRE_DECREMENTO(self, expressao):
        tipoId = ts.getBindable(expressao.id)[ts.TYPE]
        if(tipoId != ts.Numero):
           print(f'ERROR semantico: Variavel {expressao.id} deve ser do tipo numerico')
           global isFineSemantic
           isFineSemantic = False
           self.printer.visitExpressaoPRE_DECREMENTO(expressao)
    
    def visitConstanteConcreto(self, constante):
        if(constante.tipo != "ID" ):
            return constante.tipo
        else:
            if(ts.getBindable(constante.valor) == None):
                print("Erro: Variável não declarada")
                global isFineSemantic
                isFineSemantic = False
            else:
                return ts.getBindable(constante.valor)[ts.TYPE]
    
    def visitExpressaoPARENTESE(self, expressao):
        pass
   
    def visitAssignPlus(self, expMatRedu):
       tipoId = ts.getBindable(expMatRedu.id)[ts.TYPE]
       if(tipoId != ts.Numero):
           print(f'ERROR semantico: Variavel {expMatRedu.id} deve ser do tipo numerico')
           global isFineSemantic
           isFineSemantic = False
           self.printer.visitAssignPlus(expMatRedu)

       exp = expMatRedu.exp.accept(self)

       if(exp not in ts.Numero):
            print(f'ERROR semantico: Expressao deve ser do tipo numerico')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitAssignPlus(expMatRedu)
           

    def visitAssignMinus(self, expMatRedu):
       tipoId = ts.getBindable(expMatRedu.id)[ts.TYPE]
       if(tipoId != ts.Numero):
           print(f'ERROR semantico: Variavel {expMatRedu.id} deve ser do tipo numerico')
           global isFineSemantic
           isFineSemantic = False
           self.printer.visitAssignMinus(expMatRedu)

       exp = expMatRedu.exp.accept(self)

       if(exp not in ts.Numero):
            print(f'ERROR semantico: Expressao deve ser do tipo numerico')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitAssignMinus(expMatRedu)

    def visitAssignMult(self, expMatRedu):
       tipoId = ts.getBindable(expMatRedu.id)[ts.TYPE]
       if(tipoId != ts.Numero):
           print(f'ERROR semantico: Variavel {expMatRedu.id} deve ser do tipo numerico')
           global isFineSemantic
           isFineSemantic = False
           self.printer.visitAssignMult(expMatRedu)

       exp = expMatRedu.exp.accept(self)

       if(exp not in ts.Numero):
            print(f'ERROR semantico: Expressao deve ser do tipo numerico')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitAssignMult(expMatRedu)

    def visitAssigndiv(self, expMatRedu):
       tipoId = ts.getBindable(expMatRedu.id)[ts.TYPE]
       if(tipoId != ts.Numero):
           print(f'ERROR semantico: Variavel {expMatRedu.id} deve ser do tipo numerico')
           global isFineSemantic
           isFineSemantic = False
           self.printer.visitAssigndiv(expMatRedu)

       exp = expMatRedu.exp.accept(self)

       if(exp not in ts.Numero):
            print(f'ERROR semantico: Expressao deve ser do tipo numerico')
            global isFineSemantic
            isFineSemantic = False
            self.printer.visitAssigndiv(expMatRedu)
    
    def visitFor_CLIKEconcrete(self, EstruturaFOR):
        
        EstruturaFOR.declaracao.accept(self)
        tipoExp1 = EstruturaFOR.expressao1.accept(self)
        if(tipoExp1 != ts.BOOL):
            print("Erro: Expressão de controle do for deve ser booleana")
            global isFineSemantic
            isFineSemantic = False
            EstruturaFOR.expressao1.accept(self.printer)
            
        tipoExp2 = EstruturaFOR.expressao2.accept(self)
        if(tipoExp2 is not ts.Numero):
            print("Erro: Expressão de incremento do for deve ser numérica")
            global isFineSemantic
            isFineSemantic = False
            EstruturaFOR.expressao2.accept(self.printer)

        EstruturaFOR.codigo.accept(self)
    
    def visitFor_INFINITOconcrete(self, EstruturaFOR):
        
        EstruturaFOR.codigo.accept(self)

    def visitFor_WHILEconcrete(self, EstruturaFOR):
        
        tipoExp = EstruturaFOR.expressao.accept(self)
        if(tipoExp != ts.BOOL):
            print("Erro: Expressão de controle do while deve ser booleana")
            global isFineSemantic
            isFineSemantic = False
            EstruturaFOR.expressao.accept(self.printer)

        EstruturaFOR.codigo.accept(self)

    def visitEstruturaIFconcrete(self, estruturaIf):
        tipoExp = estruturaIf.expressao.accept(self)
        if(tipoExp != ts.BOOL):
            print("Erro: Expressão de controle do if deve ser booleana")
            global isFineSemantic
            isFineSemantic = False
            estruturaIf.expressao.accept(self.printer)

        estruturaIf.codigo.accept(self)

    def visitEstruturaIF_ELSEconcrete (self, estruturaElse):
        tipoExp = estruturaElse.expressao.accept(self)
        if(tipoExp != ts.BOOL):
            print("Erro: Expressão de controle do if deve ser booleana")
            global isFineSemantic
            isFineSemantic = False
            estruturaElse.expressao_else.accept(self.printer)

        estruturaElse.codigo.accept(self)
        estruturaElse.expressao_else.accept(self)
    
    def visitEstruturaELSEconcrete(self, estruturaElse):
        estruturaElse.codigo.accept(self)
    
    def visitEstruturaELSE_IFconcrete(self, estruturaElse):
        estruturaElse.estrutura_if.accept(self)
    
    def visitFuncao(self, funcao):
        ts.beginScope(funcao.id)
        funcao.codigo.accept(self)
        ts.endScope()

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

    def visitChamadaFuncao(self, ChamadaFuncao):
        if(ts.getBindable(ChamadaFuncao.nome) == None):
            print("Erro: Função não declarada" + ChamadaFuncao.nome)
            global isFineSemantic
            isFineSemantic = False
        else:
            params = ts.getBindable(ChamadaFuncao.nome)[ts.PARAMS]
            if(params != None):
                if(len(params) != len(ChamadaFuncao.parametros)):
                    print("Erro: Número de parâmetros incompatível")
                    global isFineSemantic
                    isFineSemantic = False
                else:
                    for i in range(len(params)):
                        if(params[i][1] != ChamadaFuncao.parametros[i].accept(self)):
                            print("Erro: Tipo de parâmetro incompatível")
                            global isFineSemantic
                            isFineSemantic = False
                            ChamadaFuncao.parametros[i].accept(self.printer)
            return ts.getBindable(ChamadaFuncao.nome)[ts.TYPE]

class RegistradorDeFuncao():
    def __init__(self,programa):
        self.programa = programa
    
    def registraFuncoes(self):
        if(self.programa.funcoes_codigo != None):
            self.programa.funcoes_codigo.accept(self)

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