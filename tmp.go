package main

import (
	"fmt"
)

func firstUniqChar(s string) byte {
	mp := map[rune]int{}
	for _, ch := range s {
		if _, ok := mp[ch]; ok {
			mp[ch]++
		} else {
			mp[ch] = 1
		}
	}
	return byte('a')
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

