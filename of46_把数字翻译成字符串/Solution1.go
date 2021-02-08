package main

import (
	"fmt"
)

func translateNum(num int) int {
	if num <= 9 {
		return 1
	}

	rightTwo := num % 100
	if 10 <= rightTwo && rightTwo <= 25 {
		return translateNum(num / 10) + translateNum(num / 100)
	}
	return translateNum(num / 10)
}

func test(testName string, num int, expected int) {
	res := translateNum(num)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
	nums1, expected1 := 12258, 5
	test("test1", nums1, expected1)

}

// 给定一个数字，我们按照如下规则把它翻译为字符串：
// 0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
// 一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

// 示例 1:

// 输入: 12258
// 输出: 5

// 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

// 提示：
// 0 <= num < 2*31
