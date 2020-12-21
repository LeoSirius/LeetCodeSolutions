package main

import (
	"fmt"
	"reflect"
)

func moveZeroes(nums []int)  {
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] != 0 {
			continue
		}
		firstNotZero := i+1
		for nums[firstNotZero] == 0 {
			firstNotZero++
			if firstNotZero == len(nums) {
				return
			}
		}
		nums[i], nums[firstNotZero] = nums[firstNotZero], nums[i]
		firstNotZero++
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

	nums2 := []int{1,0}
	expected2 := []int{1,0}
	test("test2", nums2, expected2)
}

// Given an array nums, write a function to move all 0's to 
// the end of it while maintaining the relative order of the non-zero elements.

// Example:

// Input: [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Note:

// You must do this in-place without making a copy of the array.
// Minimize the total number of operations.
