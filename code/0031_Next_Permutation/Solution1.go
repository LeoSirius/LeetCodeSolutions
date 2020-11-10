package main

import (
	"fmt"
	"reflect"
)

func reverse(nums []int) {
	for i, j := 0, len(nums)-1; i < j; i, j = i+1, j-1 {
		nums[i], nums[j] = nums[j], nums[i]
	}
}

func nextPermutation(nums []int)  {
	maxIdx := 0

	// 第一次遍历，找到最大值的索引
	for i := len(nums)-1; i >= 0; i-- {
		if i == 0 {
			reverse(nums)
			return
		}
		if nums[i-1] < nums[i] {
			maxIdx = i
			break
		}
	}

	// 第二次遍历，交换最大前面的一个数
	for i := len(nums)-1; i >= maxIdx; i-- {
		if (nums[maxIdx-1] < nums[i]) {
			nums[maxIdx-1], nums[i] = nums[i], nums[maxIdx-1]
			break
		}
	}

	// 第三次遍历，reverse nums[maxIdx:]
	for i, j := maxIdx, len(nums)-1; i < j; i, j = i+1, j-1 {
		nums[i], nums[j] = nums[j], nums[i]
	}
}

func test(testName string, nums, expected []int) {
	nextPermutation(nums)
	if reflect.DeepEqual(nums, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	nums1 := []int{1,2,3}
	expected1 := []int{1,3,2}
	test("test1", nums1, expected1)

	nums2 := []int{3,2,1}
	expected2 := []int{1,2,3}
	test("test2", nums2, expected2)

	nums3 := []int{1,1,5}
	expected3 := []int{1,5,1}
	test("test3", nums3, expected3)

	nums4 := []int{1}
	expected4 := []int{1}
	test("test4", nums4, expected4)
}

// Implement next permutation, which rearranges 
// numbers into the lexicographically next greater permutation of numbers.

// If such an arrangement is not possible, it must rearrange
// it as the lowest possible order (i.e., sorted in ascending order).

// The replacement must be in place and use only constant extra memory.

// Example 1:

// Input: nums = [1,2,3]
// Output: [1,3,2]

// Example 2:

// Input: nums = [3,2,1]
// Output: [1,2,3]

// Example 3:

// Input: nums = [1,1,5]
// Output: [1,5,1]

// Example 4:

// Input: nums = [1]
// Output: [1]
//  

// Constraints:

// 1 <= nums.length <= 100
// 0 <= nums[i] <= 100
