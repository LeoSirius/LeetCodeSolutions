package main

import (
	"fmt"

)

func strStr(haystack string, needle string) int {
	if haystack == needle {
		return 0
	}
	len1, len2 := len(haystack), len(needle)
	if len1 < len2 {
		return -1
	}

	start := 0
	for start < len1 {
		p1, p2 := start, 0
		for p1 < len1 && p2 < len2 && haystack[p1] == needle[p2] {
			p1++
			p2++
		}
		if p2 == len2 {
			return start
		}
		start++
	}
	return -1
}

func test(testName, haystack, needle string, expected int) {
	res := strStr(haystack, needle)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	haystack1 := "hello"
	needle1 := "ll"
	expected1 := 2
	test("test1", haystack1, needle1, expected1)

	haystack2 := "aaaaa"
	needle2 := "bba"
	expected2 := -1
	test("test2", haystack2, needle2, expected2)

	haystack3 := ""
	needle3 := ""
	expected3 := 0
	test("test3", haystack3, needle3, expected3)

}

// Implement strStr().

// Return the index of the first occurrence of needle in haystack,
//  or -1 if needle is not part of haystack.

// Clarification:

// What should we return when needle is an empty string? 
// This is a great question to ask during an interview.

// For the purpose of this problem, we will return 0 when needle is an empty string.
//  This is consistent to C's strstr() and Java's indexOf().

//  

// Example 1:

// Input: haystack = "hello", needle = "ll"
// Output: 2

// Example 2:

// Input: haystack = "aaaaa", needle = "bba"
// Output: -1

// Example 3:

// Input: haystack = "", needle = ""
// Output: 0
//  

// Constraints:

// 0 <= haystack.length, needle.length <= 5 * 104
// haystack and needle consist of only lower-case English characters.
