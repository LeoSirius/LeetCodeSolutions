package main

import (
	"fmt"
	"reflect"
)

func reverse(nums []int) {
	for l, r := 0, len(nums)-1; l < r; l, r = l+1, r-1 {
		nums[l], nums[r] = nums[r], nums[l]
	}
}


func rotate(nums []int, k int) {
	k = k % len(nums)
	reverse(nums)
	reverse(nums[:k])  // go的切片还是使用原内存，不会创建新的对象
	reverse(nums[k:])
}

func test(testName string, nums []int, k int, expected []int) {
	rotate(nums, k)
	if reflect.DeepEqual(nums, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	nums1 := []int{1,2,3,4,5,6,7}
	k1 := 3
	expected1 := []int{5,6,7,1,2,3,4}
	test("test1", nums1, k1, expected1)

	nums2 := []int{-1,-100,3,99}
	k2 := 2
	expected2 := []int{3,99,-1,-100}
	test("test2", nums2, k2, expected2)

	nums3 := []int{1,2,3,4,5,6}
	k3 := 11
	expected3 := []int{2,3,4,5,6,1}
	test("test3", nums3, k3, expected3)

}


// 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

// 示例 1:

// 输入: [1,2,3,4,5,6,7] 和 k = 3
// 输出: [5,6,7,1,2,3,4]
// 解释:
// 向右旋转 1 步: [7,1,2,3,4,5,6]
// 向右旋转 2 步: [6,7,1,2,3,4,5]
// 向右旋转 3 步: [5,6,7,1,2,3,4]

// 示例 2:

// 输入: [-1,-100,3,99] 和 k = 2
// 输出: [3,99,-1,-100]
// 解释: 
// 向右旋转 1 步: [99,-1,-100,3]
// 向右旋转 2 步: [3,99,-1,-100]

// 说明:

// 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
// 要求使用空间复杂度为 O(1) 的 原地 算法。

