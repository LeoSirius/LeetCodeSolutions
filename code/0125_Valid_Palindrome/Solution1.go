package main

import (
	"fmt"
	"unicode"
)

func isAphaNum(ch byte) bool {
	return unicode.IsDigit(rune(ch)) || unicode.IsLetter(rune(ch))
}

func isPalindrome(s string) bool {
	i, j := 0, len(s)-1
	for i < j {
		for i < j && !isAphaNum(s[i]) {i++}
		for i < j && !isAphaNum(s[j]) {j--}
		if unicode.ToLower(rune(s[i])) != unicode.ToLower(rune(s[j])) {
			return false
		}
		i++
		j--
	}
	return true
}

func test(testName string, s string, expected bool) {
	res := isPalindrome(s)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	s1 := "A man, a plan, a canal: Panama"
	expected1 := true
	test("test1", s1, expected1)

	s2 := "race a car"
	expected2 := false
	test("test2", s2, expected2)

}

// 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

// 说明：本题中，我们将空字符串定义为有效的回文串。

// 示例 1:

// 输入: "A man, a plan, a canal: Panama"
// 输出: true
// 示例 2:

// 输入: "race a car"
// 输出: false
