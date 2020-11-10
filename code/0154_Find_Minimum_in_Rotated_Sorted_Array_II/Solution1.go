package main

import (
	"fmt"
)

func findMin(nums []int) int {
	l, r := 0, len(nums)-1
	mid := 0
	for l < r {
		mid = l + (r - l) / 2
		if nums[mid] < nums[r] {
			r = mid
		} else if nums[mid] > nums[r] {
			l = mid + 1
		} else {
			r--
		}
	}
	return nums[l]
}

func test(testName string, nums []int, expected int) {
	res := findMin(nums)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	nums1 := []int{1,3,5}
	expected1 := 1
	test("test1", nums1, expected1)

	nums2 := []int{2,2,2,0,1}
	expected2 := 0
	test("test2", nums2, expected2)

}

// Suppose an array sorted in ascending order is 
// rotated at some pivot unknown to you beforehand.

// (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

// Find the minimum element.

// The array may contain duplicates.

// Example 1:

// Input: [1,3,5]
// Output: 1

// Example 2:

// Input: [2,2,2,0,1]
// Output: 0
// Note:

// This is a follow up problem to Find Minimum in Rotated Sorted Array.
// Would allow duplicates affect the run-time complexity? How and why?

