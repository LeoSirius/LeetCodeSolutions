
package main

import (
	"fmt"
	"reflect"
)

func minInt(a, b int) int {
	if (a < b) {
		return a
	}
	return b
}

func intersect(nums1 []int, nums2 []int) []int {
	mp1 := make(map[int]int)
	mp2 := make(map[int]int)
	res := []int{}

	for _, n := range(nums1) {
		if _, ok := mp1[n]; !ok {
			mp1[n] = 1
		} else {
			mp1[n]++
		}
	}
	for _, n := range(nums2) {
		if _, ok := mp2[n]; !ok {
			mp2[n] = 1
		} else {
			mp2[n]++
		}
	}

	for n, times := range mp1 {
		if val, ok := mp2[n]; ok {
			minTimes := minInt(times, val)
			for i := 0; i < minTimes; i++ {
				res = append(res, n)
			}
		}
	}

	return res
}

func test(testName string, nums1, nums2, expected []int) {
	res := intersect(nums1, nums2)
	if reflect.DeepEqual(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	nums11 := []int{1,2,2,1}
	nums21 := []int{2,2}
	expected1 := []int{2,2}
	test("test1", nums11, nums21, expected1)

	nums12 := []int{4,9,5}
	nums22 := []int{9,4,9,8,4}
	expected2 := []int{4,9}
	test("test2", nums12, nums22, expected2)

}

// 给定两个数组，编写一个函数来计算它们的交集。


// 示例 1：

// 输入：nums1 = [1,2,2,1], nums2 = [2,2]
// 输出：[2,2]

// 示例 2:

// 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// 输出：[4,9]
//  

// 说明：

// 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
// 我们可以不考虑输出结果的顺序。

// 进阶：

// 如果给定的数组已经排好序呢？你将如何优化你的算法？
// 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
// 如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
