package main

import (
	"fmt"
)

func fib(n int) int {
	a, b := 0, 1
	for i := 0; i < n; i++ {
		a, b = b, (a + b) % 1000000007
	}
	return a
}

func test(testName string, n int, expected int) {
	res := fib(n)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	n1, expected1 := 2, 1
	test("test1", n1, expected1)

	n2, expected2 := 5, 5
	test("test2", n2, expected2)

	n3, expected3 := 45, 134903163
	test("test3", n3, expected3)

}


// 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

// F(0) = 0,   F(1) = 1
// F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
// 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

// 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
