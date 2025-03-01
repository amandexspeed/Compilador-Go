package main

import "fmt"

func main() {
    a := 5
    b := 4
    fmt.Println(soma(a, b))
}

func soma(a int, b int) int {
    return a + b
}
