package main

import (
	"fmt"
)

func countAndSay(n int) string {
	if (n == 1) {return "1"}
	if (n == 2) {return "11"}
	lastSay := countAndSay(n-1)
	newSay := ""
	count := 1
	for i := 1; i < len(lastSay); i++ {
		if lastSay[i-1] == lastSay[i] {
			count++
		} else {
			newSay += fmt.Sprint(count)
			newSay += string(lastSay[i-1])
			count = 1
		}
		if i == len(lastSay)-1 {
			newSay += fmt.Sprint(count)
			newSay += string(lastSay[i])
		}
	}
	return newSay

}

func test(testName string, n int, expected string) {
	res := countAndSay(n)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	n1 := 1
	expected1 := "1"
	test("test1", n1, expected1)

	n2 := 4
	expected2 := "1211"
	test("test2", n2, expected2)

	n3 := 6
	expected3 := "312211"
	test("test3", n3, expected3)
}

