# ✨ Linguagem Go - Elementos Léxicos

Go é uma linguagem de programação de propósito geral desenvolvida pelo Google. Ela é usada para criar programas eficientes e de alto desempenho. A seguir, destacamos os elementos léxicos que formam a base da linguagem Go:

#### 1. Palavras reservadas.

Go possui um conjunto de palavras reservadas, que são usadas para definir a estrutura do código. Estas palavras não podem ser usadas como identificadores. As palavras reservadas em Go são:

break
case
chan
const
continue
default
defer
else
fallthrough
for
func
go
goto
if
import
interface
map
package
range
return
select
struct
switch
type
var

#### 2. Operadores

Go utiliza os operadores a seguir para manipulação aritmética, atribuições e comparação de valores. A tabela de precedência dos operadores é descrita a seguir:

Operadores Aritméticos:
+ (soma)
- (subtração)
* (multiplicação)
/ (divisão)
% (módulo)
^ (operação bitwise XOR ou bitwise NOT)
Operador de Atribuição:
= (atribuição)
Operadores de Comparação:
< (menor que)
> (maior que)

Grau de Precedência dos Operadores em Go
Os operadores têm diferentes níveis de precedência, o que afeta a ordem em que as expressões são avaliadas. Abaixo está a tabela de precedência de operadores, do mais alto para o mais baixo:


| Grau de Precedência |        Operador       |     Associatividade     |
|:-------------------:|:---------------------:|:-----------------------:|
|          1          |        * / %          | Esquerda para Direita   |
|          2          |        + -            | Esquerda para Direita   |
|          3          |     << >> & &^        | Esquerda para Direita   |
|          4          |     == != < <= > >=   | Esquerda para Direita   |
|          5          |         ^ |           | Esquerda para Direita   |
|          6          |          &&           | Esquerda para Direita   |
|          7          |          ||           | Esquerda para Direita   |
|          8          |          ++ --        | Direita para Esquerda   |
|          9          |          = :=         | Direita para Esquerda   |


#### 3. Delimitadores

Go utiliza os seguintes delimitadores para separar tokens no código-fonte:

**;** (ponto e vírgula) → Termina uma instrução.
**,** (vírgula) → Usado para separar parâmetros e variáveis.
**()** (parênteses) → Utilizado para expressões, como chamadas de função e controle de fluxo.
**{}** (chaves) → Define blocos de código, como os de funções e estruturas de controle.

#### 4. Identificadores

Identificadores em Go são usados para nomear variáveis, funções, tipos e outros elementos. Eles seguem estas regras:

Um identificador deve começar com uma letra (A-Z, a-z) ou o sublinhado (_).
Após o primeiro caractere, o identificador pode incluir letras, números (0-9) e sublinhados.
Exemplos de identificadores válidos:

variavel
numero2
_minha_variavel

#### 5. Números

Go oferece suporte apenas para números inteiros. Não há suporte para números com sinal explícito (positivo ou negativo) nem números de ponto flutuante.

Exemplos de números válidos:

100
2000
30

#### 6. Erros

Qualquer sequência de caracteres que não se enquadre em nenhuma das categorias acima será considerado um erro léxico. Isso pode incluir caracteres inválidos ou palavras desconhecidas para o lexer.

### 7. Espaços em Branco e Quebras de Linha

Espaços em branco e tabulações são ignorados pela análise léxica.
Quebras de linha são importantes para determinar em qual linha o lexer está durante a análise e são registradas na variável lineno.
