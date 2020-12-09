package main

import (
	"fmt"
)

func uniquePaths(m int, n int) int {
	dp := make([]int, n)
	dp[0] = 1
	for i := 0; i < m; i++ {
		for j := 1; j < n; j++ {
			dp[j] += dp[j-1]
		}
	}
	return dp[len(dp)-1]
}

func test(testName string, m, n, expected int) {
	res := uniquePaths(m, n)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	m1, n1, expected1 := 3, 2, 3
	test("test1", m1, n1, expected1)

	m2, n2, expected2 := 7, 3, 28
	test("test2", m2, n2, expected2)
}


