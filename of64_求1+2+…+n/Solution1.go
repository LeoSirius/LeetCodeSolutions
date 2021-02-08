package main

import (
    "fmt"
)

func sumNums(n int) int {
    res := 0

    var sum func(int) bool
    sum = func(n int) bool {
        res += n
        return n > 0 && sum(n-1)
    }
    sum(n)
    return res
}


func test(testName string, n, expected int) {
    res := sumNums(n)
    if res == expected {
        fmt.Println(testName + " success.")
    } else {
        fmt.Println(testName + " failed.")
    }
}

func main() {
    n1, expected1 := 3, 6
    test("test1", n1, expected1)

    n2, expected2 := 9, 45
    test("test2", n2, expected2)
}

// 求 1+2+...+n ，
// 要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

// 示例 1：
// 输入: n = 3
// 输出: 6

// 示例 2：
// 输入: n = 9
// 输出: 45
 

// 限制：

// 1 <= n <= 10000