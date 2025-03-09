package testeCompilador

import "fmt"

func init() {
    a := 5
    b := 4
    soma(a, b)
    for a=0;a<10;a++{
		b++
	}
}

func soma(a int, b int) int {
    return a + b
}
