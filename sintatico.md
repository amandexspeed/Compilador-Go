## Documentação Sintática da linguagem Go
## 1.Elementos Sintáticos
Um programa em Go é composto por uma ou mais funções, entre elas a main. Sua sintaxe é apresentada na seguinte regra:
funcao -> func ID ""(" sigParams ")"" retorno "{" stms "}"
Onde  ID é o nome da função. sigParams representa os argumentos da função, composto por um identificador e um tipo de parametro. 
Retorno é o tpo de retorno da função. E por fm tem o stms que representam os comados.
A próxima seção apresenta os comandos da linguagem go.

## 1.1 Comandos da Linguagem Go

Go lida com comandos de expressões,condicionais, return e de repetição, conforme apresentado nas seguintes regras:
  stm -> exp
    |for  exp  "{" stm "}"
    |for exp ";" exp ";" exp "{" stm "}"
    |if  exp  "{" stm "}"
    |switch exp ";" ID "{" [case stm] default stm"}"
    |return [retorno] 

## 1.2 Expressões em Go

Go dá suporte a expressões aritmétricas de adição, subtração, multiplicação, divisão e módulo(resto da divisão), também dá suporte a chamadas de função (call), atribuição de valores a variáveis (assign). Por fim, expressões também podem ser números (NUM) e variáveis (ID). A sintaxe das expressões é apresentada pela seguinte regra:
  exp → exp "+" exp | 
      exp "-" exp | 
      exp "*" exp |
      exp "/" exp |
      exp "%" exp |
      call | 
      assign | 
      NUM | 
      ID
      
## 1.2.1 Chamadas de Função e Atribuição

Go dá suporte a chamadas de função com e sem parâmetros. Adicionalmente, Go permite atribuir valores a variáveis, conforme as regras apresentadas a seguir:
  call → ID "("params")" | 
       ID "(" ")"
  params → exp"," params | 
        exp
  assign → ID "=" exp

## Exemplos de Código

Exemplo 1:

package main

import "fmt"

func main() {
    fmt.Println("Olá")
}

Exemplo 2:
package main

import "fmt"
func potencia ( x int, y int) int {
  for i:= 0; i<y; i++ {
    x *= x
  }
  return x
}
func main() {
    fmt.Println(potencia(2,3))
}
    
