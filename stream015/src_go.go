package main

import "os"
import "fmt"
import "strconv"

func main() {
    if len(os.Args) < 3 {
        fmt.Println("this program needs 2 arguments to run")
    }

    start_num, _ := strconv.Atoi(os.Args[1])
    count, _ := strconv.Atoi(os.Args[2])

    var list []int

    for i := 0; i < count; i++ {
        list = append(list, i * start_num)
    }

    sum := 0
    divisible := 0

    for _, num := range list {
        sum += num
        if num % 10 == 0 {
            divisible++
        }
    }

    fmt.Println(sum, divisible)
}
