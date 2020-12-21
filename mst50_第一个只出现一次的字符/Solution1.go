package main

import (
	"fmt"
)

func firstUniqChar(s string) byte {
	list := [26]int{}
	for _, ch := range s {
		list[ch-'a']++
	}

	// 题目要求找出第一个只出现一次的字符
	// 第二次遍历判断的时候，还是按照s中的顺序
	for _, ch := range s {
		if list[ch-'a'] == 1 {
			return byte(ch)
		}
	}

	return byte(' ')
}

func test(testName string, s string, expected byte) {
	res := firstUniqChar(s)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	s1 := "abaccdeff"
	expected1 := byte('b')
	test("test1", s1, expected1)

	s2 := ""
	expected2 := byte(' ')
	test("test2", s2, expected2)

	s3 := "loveleetcode"
	expected3 := byte('v')
	test("test3", s3, expected3)

}


// 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

// 示例:
// s = "abaccdeff"
// 返回 "b"

// s = "" 
// 返回 " "
//  

// 限制：
// 0 <= s 的长度 <= 50000

