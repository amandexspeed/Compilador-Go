package main

import "fmt"

func main() {
    fmt.Println("Iniciando os testes de laços 'for' com condição.")

    testeIdentificadoresPalavrasReservadas()
    testeOperadoresRelacionaisLogicos()
    testeEscopos()
    testeIncrementoDecremento()
    testeExpressoesComplexas()
    testeFuncoesStrings()
    testeNumerosInteirosPontoFlutuante()
    testeComentarios()
    testeErrosLexicos()
    testeCasosLimite()

    fmt.Println("Todos os testes foram finalizados!")
}

// 1. Identificadores e palavras reservadas
func testeIdentificadoresPalavrasReservadas() {
    fmt.Println("Teste: Identificadores e palavras reservadas")

    x := 0
    for x < 3 {
        fmt.Println("x:", x)
        x++
    }
}

// 2. Operadores relacionais e lógicos
func testeOperadoresRelacionaisLogicos() {
    fmt.Println("Teste: Operadores relacionais e lógicos")

    i := 0
    for i >= 0 && i < 5 {
        fmt.Println("i (>= e <):", i)
        i++
    }

    for i != 8 {
        fmt.Println("i (!=):", i)
        i += 3
    }
}

// 3. Escopos com { e }
func testeEscopos() {
    fmt.Println("Teste: Escopos com { e }")

    for i := 0; i < 2; i++ {
        {
            fmt.Println("Escopo interno: i =", i)
        }
    }
}

// 4. Incremento e decremento
func testeIncrementoDecremento() {
    fmt.Println("Teste: Incremento e decremento")

    x := 5
    for x > 0 {
        fmt.Println("Decremento x:", x)
        x--
    }

    for x < 5 {
        fmt.Println("Incremento x:", x)
        x++
    }
}

// 5. Expressões mais complexas
func testeExpressoesComplexas() {
    fmt.Println("Teste: Expressões mais complexas")

    y := 0
    for y*y < 16 {
        fmt.Println("y^2:", y*y)
        y++
    }
}

// 6. Funções e strings
func testeFuncoesStrings() {
    fmt.Println("Teste: Funções e strings")

    palavra := "Go"
    for len(palavra) < 6 {
        fmt.Println("Palavra:", palavra)
        palavra += "!"
    }
}

// 7. Números inteiros e ponto flutuante
func testeNumerosInteirosPontoFlutuante() {
    fmt.Println("Teste: Números inteiros e ponto flutuante")

    for x := 0; x < 3; x++ {
        fmt.Println("Inteiro x:", x)
    }

    f := 0.5
    for f < 2.0 {
        fmt.Printf("Ponto flutuante f: %.2f\n", f)
        f += 0.5
    }
}

// 8. Comentários (// e /* ... */)
func testeComentarios() {
    fmt.Println("Teste: Comentários (// e /* ... */)")

    x := 0 // Incremento até 3
    for x < 3 {
        /* Comentário multi-linha
           explicando o código */
        fmt.Println("x:", x)
        x++
    }
}

// 9. Erros léxicos
func testeErrosLexicos() {
    fmt.Println("Teste: Erros léxicos")

    // Este teste é apenas simulado, pois código com erros não compila.
    fmt.Println("Erro léxico seria, por exemplo, usar uma palavra reservada incorretamente.")
}

// 10. Casos limite (corpos vazios, condições inválidas, etc.)
func testeCasosLimite() {
    fmt.Println("Teste: Casos limite")

    // Corpo vazio
    for i := 0; i < 3; i++ {
        // Sem instruções no corpo do loop
    }
    fmt.Println("Loop com corpo vazio executado com sucesso.")

    // Condições inválidas (exemplo de prática incorreta)
    // for ; ; {
    //     break // Seria um loop infinito se não fosse interrompido
    // }

    fmt.Println("Casos limite verificados.")
}
