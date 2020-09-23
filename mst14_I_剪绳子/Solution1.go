package main

import (
    "fmt"
    "math"
)

func cuttingRope(n int) int {
    var dp = make([]int, n+1)
    dp[0], dp[1] = 1, 1

    for i := 2; i <= n; i++ {
        for j := 1; j < i; j++ {
            max1 := math.Max(float64(j * (i - j)), float64(j * dp[i-j]))
            dp[i] = int(math.Max(float64(dp[i]), max1))
        }
    }
    return dp[n]
}

func test(testName string, n int, expected int) {
    res := cuttingRope(n)
    if res == expected {
        fmt.Println(testName + " success.")
    } else {
        fmt.Println(testName + " failed.")
    }
}

func main() {
    n1, expected1 := 2, 1
    test("test1", n1, expected1)

    n2, expected2 := 10, 36
    test("test2", n2, expected2)
}

// 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
// 每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
// 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

// 示例 1：

// 输入: 2
// 输出: 1
// 解释: 2 = 1 + 1, 1 × 1 = 1

// 示例 2:
// 输入: 10
// 输出: 36
// 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

// 提示：

// 2 <= n <= 58
