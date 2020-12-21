package main

import (
	"fmt"
)

func countPrimes(n int) int {
	isPrime := make([]bool, n)
	for i := range isPrime {
		isPrime[i] = true
	}
	cnt := 0

	for i := 2; i < n; i++ {
		if isPrime[i] {
			cnt++
		}
		for j := 2*i; j < n; j += i {
			isPrime[j] = false
		}
	}
	return cnt
}

func test(testName string, n, expected int) {
	res := countPrimes(n)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	n1 := 10
	expected1 := 4
	test("test1", n1, expected1)

	n2 := 0
	expected2 := 0
	test("test1", n2, expected2)

	n3 := 1
	expected3 := 0
	test("test3", n3, expected3)
}


// 统计所有小于非负整数 n 的质数的数量。

// 示例 1：

// 输入：n = 10
// 输出：4
// 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

// 示例 2：

// 输入：n = 0
// 输出：0

// 示例 3：

// 输入：n = 1
// 输出：0
 

// 提示：

// 0 <= n <= 5 * 10^6