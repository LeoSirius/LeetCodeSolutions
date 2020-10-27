package main

import (
	"fmt"
)

func numWays(n int) int {
	a, b := 0, 1
	for i := 0; i < n; i++ {
		a, b = b, (a + b) % 1000000007
	}
	return b
}

func test(testName string, n int, expected int) {
	res := numWays(n)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	n1, expected1 := 2, 2
	test("test1", n1, expected1)

	n2, expected2 := 7, 21
	test("test2", n2, expected2)

	n3, expected3 := 0, 1
	test("test3", n3, expected3)

}

// 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

// 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

// 示例 1：

// 输入：n = 2
// 输出：2
// 示例 2：

// 输入：n = 7
// 输出：21
// 示例 3：

// 输入：n = 0
// 输出：1
// 提示：

// 0 <= n <= 100

