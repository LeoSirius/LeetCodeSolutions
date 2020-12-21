package main

import (
	"fmt"
	"reflect"
)

func twoSum(nums []int, target int) []int {
	mp := make(map[int]bool)

	for _, n := range nums {
		num2find := target - n
		if mp[num2find] {
			return []int{n, num2find}
		}
		mp[n] = true
	}
	return []int{}
}

func test(testName string, nums []int, target int, expectedArr1 [][]int) {
	res := twoSum(nums, target)
	fmt.Printf("res = %v\n", res)
	for _, pair := range expectedArr1 {
		if reflect.DeepEqual(res, pair) {
			fmt.Println(testName + " success.")
			return
		}
	}
	fmt.Println(testName + " failed.")
}

func main() {
	nums1 := []int{2,7,11,15}
	target1 := 9
	expectedArr1 := [][]int{
		{2,7},
		{7,2},
	}
	test("test1", nums1, target1, expectedArr1)

	nums2 := []int{10,26,30,31,47,60}
	target2 := 40
	expectedArr2 := [][]int{
		{10, 30},
		{30, 10},
	}
	test("test2", nums2, target2, expectedArr2)

}


// 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
// 如果有多对数字的和等于s，则输出任意一对即可。

// 示例 1：

// 输入：nums = [2,7,11,15], target = 9
// 输出：[2,7] 或者 [7,2]

// 示例 2：

// 输入：nums = [10,26,30,31,47,60], target = 40
// 输出：[10,30] 或者 [30,10]
//  

// 限制：

// 1 <= nums.length <= 10^5
// 1 <= nums[i] <= 10^6

