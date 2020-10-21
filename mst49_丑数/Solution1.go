package main

import (
	"fmt"
)

func minOf(nums ...int) int {
	min := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] < min {
			min = nums[i]
		}
	}
	return min
}

func nthUglyNumber(n int) int {
	if n <= 1 {
		return n
	}

	dp := make([]int, n)
	dp[0] = 1
	p2, p3, p5 := 0, 0, 0
	for i := 1; i < n; i++ {
		dp[i] = minOf(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)

		if dp[i] == dp[p2] * 2 {
			p2++
		}
		if dp[i] == dp[p3] * 3 {
			p3++
		}
		if dp[i] == dp[p5] * 5 {
			p5++
		}
	}
	return dp[n-1]
}

func test(testName string, n int, expected int) {
	res := nthUglyNumber(n)
	fmt.Printf("res = %v\n", res)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	n1, expected1 := 10, 12
	test("test1", n1, expected1)
}


// 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

// 示例:

// 输入: n = 10
// 输出: 12
// 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
// 说明:  

// 1 是丑数。
// n 不超过1690。

