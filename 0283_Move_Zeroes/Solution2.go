package main

import (
	"fmt"
	"reflect"
)

func moveZeroes(nums []int)  {
	tail := 0
	for _, v := range(nums) {
		if v != 0 {
			nums[tail] = v
			tail++
		}
	}
	for tail < len(nums) {
		nums[tail] = 0
		tail++
	}
}

func test(testName string, nums, expected []int) {
	moveZeroes(nums)
	if reflect.DeepEqual(nums, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	nums1 := []int{0,1,0,3,12}
	expected1 := []int{1,3,12,0,0}
	test("test1", nums1, expected1)
}

// Given an array nums, write a function to move all 0's to 
// the end of it while maintaining the relative order of the non-zero elements.

// Example:

// Input: [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Note:

// You must do this in-place without making a copy of the array.
// Minimize the total number of operations.
