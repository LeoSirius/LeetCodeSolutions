package main

import (
    "fmt"
)

func hammingWeight(num uint32) int {
    res := 0
    for 0 < num {
        res += int(num & 1)
        num = num >> 1
    }
    return res
}

func test(testName string, num uint32, expected int) {
    res := hammingWeight(num)
    if res == expected {
        fmt.Println(testName + " success.")
    } else {
        fmt.Println(testName + " failed.")
    }
}

func main() {
    var num1 uint32 = 11
    expected1 := 3
    test("test1", num1, expected1)

    var num2 uint32 = 128
    expected2 := 1
    test("test2", num2, expected2)

    var num3 uint32 = 4294967293
    expected3 := 31
    test("test3", num3, expected3)
}


// 请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，
// 把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

// 示例 1：

// 输入：00000000000000000000000000001011
// 输出：3
// 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 "1"。
// 示例 2：

// 输入：00000000000000000000000010000000
// 输出：1
// 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 "1"。
// 示例 3：

// 输入：11111111111111111111111111111101
// 输出：31
// 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 "1"。