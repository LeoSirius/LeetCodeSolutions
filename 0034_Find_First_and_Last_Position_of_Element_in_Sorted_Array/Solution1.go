package main

import (
	"fmt"
	"reflect"
)

func searchRange(nums []int, target int) []int {
	res := []int{-1,-1}
	if len(nums) == 0 {
		return res
	}

	l, r := 0, len(nums)-1
	for l < r {
		m := l + (r-l)/2
		if nums[m] < target {
			l = m + 1
		} else {
			r = m
		}
	}

	if nums[l] != target {
		return res
	}
	res[0] = l
	r = len(nums)-1

	for l < r {
		m := l + (r-l)/2 + 1     // 必须，让mid偏向右边。
		if nums[m] > target {
			r = m - 1
		} else {
			l = m
		}
	}
	res[1] = r

	return res
}

func test(testName string, nums []int, target int, expected []int) {
	res := searchRange(nums, target)
	if reflect.DeepEqual(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	nums1 := []int{5,7,7,8,8,10}
	target1 := 8
	expected1 := []int{3, 4}
	test("test1", nums1, target1, expected1)

	nums2 := []int{5,7,7,8,8,10}
	target2 := 6
	expected2 := []int{-1, -1}
	test("test2", nums2, target2, expected2)

	nums3 := []int{}
	target3 := 0
	expected3 := []int{-1,-1}
	test("test3", nums3, target3, expected3)

}

// 给定一个按照升序排列的整数数组 nums，和一个目标值 target。
// 找出给定目标值在数组中的开始位置和结束位置。

// 如果数组中不存在目标值 target，返回 [-1, -1]。

// 进阶：

// 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
//  
// 示例 1：

// 输入：nums = [5,7,7,8,8,10], target = 8
// 输出：[3,4]

// 示例 2：

// 输入：nums = [5,7,7,8,8,10], target = 6
// 输出：[-1,-1]

// 示例 3：

// 输入：nums = [], target = 0
// 输出：[-1,-1]
//  

// 提示：

// 0 <= nums.length <= 105
// -109 <= nums[i] <= 109
// nums 是一个非递减数组
// -109 <= target <= 109


