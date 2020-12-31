package main

import (
	"fmt"
)

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	} else if len(strs) == 1 {
		return strs[0]
	}

	// 加一个minLen的判断，处理特殊情况，防止下面p越界
	minLen := len(strs[0])
	for _, str := range(strs) {
		if minLen > len(str) {
			minLen = len(str)
		}
	}
	p := 0
	for {
		if p == minLen {
			return strs[0][:minLen]
		}
		ch := strs[0][p]
		isColSame := true
		for _, str := range(strs) {
			if str[p] != ch {
				isColSame = false
			}
		}
		if !isColSame {
			break
		}
		p++
	}
	return strs[0][:p]
}

func test(testName string, strs []string, expected string) {
	res := longestCommonPrefix(strs)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
	strs1 := []string{"flower", "flow", "flight"}
	expected1 := "fl"
	test("test1", strs1, expected1)

	strs2 := []string{}
	expected2 := ""
	test("test2", strs2, expected2)

	strs3 := []string{"", ""}
	expected3 := ""
	test("test3", strs3, expected3)

	strs4 := []string{"ab", "a"}
	expected4 := "a"
	test("test4", strs4, expected4)

	strs5 := []string{"flower","flower","flower","flower"}
	expected5 := "flower"
	test("test5", strs5, expected5)

}
