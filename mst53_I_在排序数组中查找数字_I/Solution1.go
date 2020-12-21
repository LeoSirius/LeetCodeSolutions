package main

import (
	"fmt"
)

func search(nums []int, target int) int {
	count := 0
	for _, n := range nums {
		if n == target {
			count++
		}
	}
	return count
}

func test(testName string, nums []int, target, expected int) {
	res := search(nums, target)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
	nums1 := []int{5,7,7,8,8,10}
	target1 := 8
	expected1 := 2
	test("test1", nums1, target1, expected1)

	nums2 := []int{5,7,7,8,8,10}
	target2, expected2 := 6, 0
	test("test2", nums2, target2, expected2)

}

// 统计一个数字在排序数组中出现的次数。

// 示例 1:

// 输入: nums = [5,7,7,8,8,10], target = 8
// 输出: 2

// 示例 2:

// 输入: nums = [5,7,7,8,8,10], target = 6
// 输出: 0
//  

// 限制：

// 0 <= 数组长度 <= 50000

