package main

import (
	"fmt"
	"strings"
	"unicode"
	"math"
)

func myAtoi(s string) int {
	i := 0
	res := 0

	// skip ' ' prefix
	if strings.HasPrefix(s, " ") {
		for i < len(s) && s[i] == ' ' {
			i++
		}
	}
	if i == len(s) {
		return 0
	}

	isPos := true
	if s[i] == '-' || s[i] == '+' {
		if s[i] == '-' {
			isPos = false
		}
		i++
	}

	for ; i < len(s) && unicode.IsDigit(rune(s[i])); i++ {
		curNum := int(s[i] - '0')
		if res > math.MaxInt32 / 10 || (res == math.MaxInt32 / 10 && curNum > 7) {
			if isPos {
				return math.MaxInt32
			} else {
				return math.MinInt32
			}
		}
		res = res * 10 + curNum
	}

	if isPos {
		return res
	}
	return -res
}

func test(testName string, s string, expected int) {
	res := myAtoi(s)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	s1 := "42"
	expected1 := 42
	test("test1", s1, expected1)

	s2 := "   -42"
	expected2 := -42
	test("test2", s2, expected2)

	s3 := "4193 with words"
	expected3 := 4193
	test("test3", s3, expected3)

	s4 := "-91283472332"
	expected4 := -2147483648
	test("test4", s4, expected4)

	s5 := ""
	expected5 := 0
	test("test5", s5, expected5)

}

// 请你来实现一个 atoi 函数，使其能将字符串转换成整数。

// 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
// 接下来的转化规则如下：

// 如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，
// 形成一个有符号整数。
// 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
// 该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，
// 它们对函数不应该造成影响。
// 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，
// 则你的函数不需要进行转换，即无法进行有效转换。

// 在任何情况下，若函数不能进行有效的转换时，请返回 0 。

// 提示：

// 本题中的空白字符只包括空格字符 ' ' 。
// 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。
// 如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
//  

// 示例 1:

// 输入: "42"
// 输出: 42

// 示例 2:

// 输入: "   -42"
// 输出: -42
// 解释: 第一个非空白字符为 '-', 它是一个负号。
//      我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

// 示例 3:

// 输入: "4193 with words"
// 输出: 4193
// 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

// 示例 4:

// 输入: "words and 987"
// 输出: 0
// 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
// 	 因此无法执行有效的转换。

// 示例 5:

// 输入: "-91283472332"
// 输出: -2147483648
// 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
//      因此返回 INT_MIN (−231) 。

