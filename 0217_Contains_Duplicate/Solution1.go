package main

import (
	"fmt"
)

func containsDuplicate(nums []int) bool {
	set := make(map[int]bool)
	for _, v := range(nums) {
		if _, ok := set[v]; ok {
			return true
		}
		set[v] = true
	}
	return false
}

func test(testName string, nums []int, expected bool) {
	res := containsDuplicate(nums)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	nums1 := []int{1,2,3,1}
	expected1 := true
	test("test1", nums1, expected1)

	nums2 := []int{1,2,3,4}
	expected2 := false
	test("test2", nums2, expected2)

	nums3 := []int{1,1,1,3,3,4,3,2,4,2}
	expected3 := true
	test("test3", nums3, expected3)
}


// Given an array of integers, find if the array contains any duplicates.

// Your function should return true if any value appears at least twice 
// in the array, and it should return false if every element is distinct.

// Example 1:

// Input: [1,2,3,1]
// Output: true
// Example 2:

// Input: [1,2,3,4]
// Output: false
// Example 3:

// Input: [1,1,1,3,3,4,3,2,4,2]
// Output: true
