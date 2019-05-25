package main

import (
    "C"
    "fmt"
)

//export Hello
func Hello() {
    fmt.Println("hello from go!")
}

//export Sum
func Sum(a int, b int) int {
    return a + b
}

func main() {}
