package main

import (
	"fmt"
)

func findRepeatNumber(nums []int) int {
	for i, v := range nums {
		for nums[i] != i {
			if nums[i] == nums[nums[i]] {
				return v
			}
			a, b := nums[i], nums[nums[i]]
			nums[i], nums[nums[i]] = b, a
		}
	}
	return -1
}


func test(testName string, nums []int, expected []int) {
	res := findRepeatNumber(nums)
	isIn := false
	for _, n := range expected {
		if n == res {
			isIn = true
			break
		}
	}
	if isIn {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
	nums1 := []int{2, 3, 1, 0, 2, 5, 3}
	expected1 := []int{2,3}
	test("test1", nums1, expected1)
}



// [2, 3, 1, 0, 2, 5, 3]
// 输出：2 或 3 

// 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
// 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
// 请找出数组中任意一个重复的数字。

// 限制：

// 2 <= n <= 100000

