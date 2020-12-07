package main

import (
	"fmt"
	"reflect"
)

func plusOne(digits []int) []int {
	carry := 1
	for i := len(digits)-1; i >= 0 && carry > 0; i-- {
		curSum := digits[i] + carry
		carry = curSum / 10
		digits[i] = curSum % 10
	}
	if carry > 0 {
		digits = append([]int{1}, digits...)
	}
	return digits
}


func test(testName string, digits, expected []int) {
	res := plusOne(digits)
	if reflect.DeepEqual(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
	digits1 := []int{1,2,3}
	expected1 := []int{1,2,4}
	test("test1", digits1, expected1)

	digits2 := []int{4,3,2,1}
	expected2 := []int{4,3,2,2}
	test("test2", digits2, expected2)

	digits3 := []int{0}
	expected3 := []int{1}
	test("test3", digits3, expected3)

	digits4 := []int{9}
	expected4 := []int{1,0}
	test("test4", digits4, expected4)

}


// Given a non-empty array of decimal digits representing a non-negative 
// integer, increment one to the integer.

// The digits are stored such that the most significant digit is 
// at the head of the list, and each element in the array contains a single digit.

// You may assume the integer does not contain any leading zero, 
// except the number 0 itself.

// Example 1:

// Input: digits = [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.

// Example 2:

// Input: digits = [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: The array represents the integer 4321.

// Example 3:

// Input: digits = [0]
// Output: [1]
//  

// Constraints:

// 1 <= digits.length <= 100
// 0 <= digits[i] <= 9


