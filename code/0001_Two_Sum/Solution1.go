package main

import (
	"fmt"
	"reflect"
	"sort"
)

func twoSum(nums []int, target int) []int {
	num2idx := make(map[int]int)

	for i, v := range(nums) {
		num2find := target - v
		if idx, ok := num2idx[num2find]; ok {
			return []int{i, idx}
		}
		num2idx[v] = i
	}
	return []int{}
}

func test(testName string, nums []int, target int, expected []int) {
	res := twoSum(nums, target)
	sort.Ints(res)
	sort.Ints(expected)
	if reflect.DeepEqual(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
	nums1 := []int{2, 7, 11, 15}
	target1 := 9
	expected1 := []int{0, 1}
	test("test1", nums1, target1, expected1)
}

// 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，
// 并返回他们的数组下标。

// 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

//  

// 示例:

// 给定 nums = [2, 7, 11, 15], target = 9

// 因为 nums[0] + nums[1] = 2 + 7 = 9
// 所以返回 [0, 1]


