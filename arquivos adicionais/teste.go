package main

import "fmt"

/*
	Olá, me chamo amanda
*/

func funcFor() {

    i := 1
    for i <= 3 {
        fmt.Println(i)
        i = i + 1
    }

    for j := 0; j < 3; j++ {
        fmt.Println(j)
    }

    for i := range 3 {
        fmt.Println("range", i)
    }

    for {
        fmt.Println("loop")
        break
    }

    for n := range 6 {
        if n%2 == 0 {
            continue
        }
        fmt.Println(n)
    }
}

func FuncIf() {
    if pA,pB := "Amanda","Bruna"; pA == pB {
        fmt.Println("São xarás!")
    } else {
        fmt.Println("São pessoas diferentes!")
    } 
}
