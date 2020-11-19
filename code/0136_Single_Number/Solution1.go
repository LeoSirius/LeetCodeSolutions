package main

import "fmt"

func singleNumber(nums []int) int {
	res := 0
	for _, n := range(nums) {
		res ^= n
	}
	return res
}

func test(testName string, nums []int, expected int) {
	res := singleNumber(nums)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	nums1 := []int{2,2,1}
	expected1 := 1
	test("test1", nums1, expected1)

	nums2 := []int{4,1,2,1,2}
	expected2 := 4
	test("test2", nums2, expected2)

	nums3 := []int{1}
	expected3 := 1
	test("test3", nums3, expected3)
}

// Given a non-empty array of integers nums, every element appears 
// twice except for one. Find that single one.

// Follow up: Could you implement a solution with a linear runtime 
// complexity and without using extra memory?

//  

// Example 1:

// Input: nums = [2,2,1]
// Output: 1

// Example 2:

// Input: nums = [4,1,2,1,2]
// Output: 4

// Example 3:

// Input: nums = [1]
// Output: 1
//  

// Constraints:

// 1 <= nums.length <= 3 * 104
// -3 * 104 <= nums[i] <= 3 * 104
// Each element in the array appears twice except for one element which 
// appears only once.
