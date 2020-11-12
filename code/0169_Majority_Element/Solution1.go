package main

import (
	"fmt"
)


func majorityElement(nums []int) int {
	count, candidate := 0, 0

	for _, n := range nums {
		if count == 0 {
			candidate = n
		}
		if candidate == n {
			count++
		} else {
			count--
		}
	}
	return candidate
}


func test(testName string, nums []int, expected int) {
	res := majorityElement(nums)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
	nums1 := []int{3,2,3}
	expected1 := 3
	test("test1", nums1, expected1)

	nums2 := []int{2,2,1,1,1,2,2}
	expected2 := 2
	test("test2", nums2, expected2)

}

// Given an array of size n, find the majority element. 
// The majority element is the element that appears more than ⌊ n/2 ⌋ times.

// You may assume that the array is non-empty and the majority 
// element always exist in the array.

// Example 1:

// Input: [3,2,3]
// Output: 3

// Example 2:

// Input: [2,2,1,1,1,2,2]
// Output: 2

