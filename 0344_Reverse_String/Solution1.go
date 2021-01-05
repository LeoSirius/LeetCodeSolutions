package main

import (
	"fmt"
	"reflect"
)

func reverseString(s []byte)  {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
}

func test(testName string, s []byte, expected []byte) {
	reverseString(s)
	if reflect.DeepEqual(s, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	s1 := []byte{'h','e','l','l','o'}
	expected1 := []byte{'o','l','l','e','h'}
	test("test1", s1, expected1)

	s2 := []byte{'H','a','n','n','a','h'}
	expected2 := []byte{'h','a','n','n','a','H'}
	test("test2", s2, expected2)

}
