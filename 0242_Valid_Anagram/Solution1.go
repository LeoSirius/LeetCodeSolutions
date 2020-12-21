package main

import (
	"fmt"
)

func isAnagram(s string, t string) bool {
	mp := make(map[rune]int)
	for _, ch := range(s) {
		mp[ch]++
	}
	for _, ch := range(t) {
		mp[ch]--
	}
	for _, v := range(mp) {
		if v != 0 {
			return false
		}
	}
	return true
}

func test(testName, s, t string, expected bool) {
	res := isAnagram(s, t)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	s1, t1 := "anagram", "nagaram"
	expected1 := true
	test("test1", s1, t1, expected1)

	s2, t2 := "rat", "car"
	expected2 := false
	test("test2", s2, t2, expected2)

}




// Given two strings s and t , write a function to determine
//  if t is an anagram of s.

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true

// Example 2:

// Input: s = "rat", t = "car"
// Output: false
// Note:
// You may assume the string contains only lowercase alphabets.

// Follow up:
// What if the inputs contain unicode characters? How would you adapt
//  your solution to such case?