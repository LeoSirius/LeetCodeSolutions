package main

import (
	"fmt"
	"math"
)

func reverse(x int) int {
	res := 0

	for x != 0 {
		n := x % 10
		x /= 10

		if res > math.MaxInt32/10 || (res == math.MaxInt32/10 && n > 7) {
			return 0
		}

		if res < math.MinInt32/10 || (res == math.MinInt32/10 && n < -8) {
			return 0
		}
		res = res * 10 + n
	}
	return res
}

func test(testName string, x, expected int) {
	res := reverse(x)
	fmt.Printf("res = %v\n", res)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	x1, expected1 := 123, 321
	test("test1", x1, expected1)

	x2, expected2 := -1234, -4321
	test("test2", x2, expected2)

	x3, expected3 := 120, 21
	test("test3", x3, expected3)
}

// 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

// 示例 1:

// 输入: 123
// 输出: 321

//  示例 2:

// 输入: -123
// 输出: -321

// 示例 3:

// 输入: 120
// 输出: 21

// 注意:

// 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
// 请根据这个假设，如果反转后整数溢出那么就返回 0。

