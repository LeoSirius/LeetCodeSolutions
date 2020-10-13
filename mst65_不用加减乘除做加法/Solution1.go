package main

import (
    "fmt"
)

func add(a int, b int) int {
    carry := 0
    for b != 0 {
        carry = (a & b) << 1
        a, b = a^b, carry
    }
    return a
}

func test(testName string, a, b, expected int) {
    res := add(a, b)
    if res == expected {
        fmt.Println(testName + " success.")
    } else {
        fmt.Println(testName + " failed.")
    }
}

func main() {
    a1, b1 := 1, 1
    expected1 := 2
    test("test1", a1, b1, expected1)

    a2, b2 := -1, 2
    expected2 := 1
    test("test2", a2, b2, expected2)
}



// 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

//  

// 示例:

// 输入: a = 1, b = 1
// 输出: 2
//  

// 提示：

// a, b 均可能是负数或 0
// 结果不会溢出 32 位整数
