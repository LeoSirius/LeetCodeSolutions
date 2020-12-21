package main

import (
	"fmt"
	"reflect"
)

func maxSlidingWindow(nums []int, k int) []int {
	deq, res := []int{}, []int{}

	for i := 0; i < len(nums); i++ {
		for len(deq) > 0 && nums[deq[len(deq)-1]] < nums[i] {
			deq = deq[:len(deq)-1]
		}
		// i + 1 - k 就是当前loop的窗口头的索引
		// 如i = 2, k = 3, i + 1 - k = 0
		// 说明，第三次loop时，k是3，包含前三个，刚好从第一个开始
		if len(deq) > 0 && deq[0] < i + 1 - k {
			deq = deq[1:]
		}

		deq = append(deq, i)

		if k - 1 <= i {
			res = append(res, nums[deq[0]])
		}
	}
	return res
}

func test(testName string, nums []int, k int, expected []int) {
	res := maxSlidingWindow(nums, k)
	fmt.Printf("res = %v\n", res)
	if reflect.DeepEqual(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
	nums1 := []int{1,3,-1,-3,5,3,6,7}
	k1 := 3
	expected1 := []int{3,3,5,5,6,7}
	test("test1", nums1, k1, expected1)

}


// 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

// 示例:

// 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
// 输出: [3,3,5,5,6,7] 
// 解释: 

//   滑动窗口的位置                最大值
// ---------------               -----
// [1  3  -1] -3  5  3  6  7       3
//  1 [3  -1  -3] 5  3  6  7       3
//  1  3 [-1  -3  5] 3  6  7       5
//  1  3  -1 [-3  5  3] 6  7       5
//  1  3  -1  -3 [5  3  6] 7       6
//  1  3  -1  -3  5 [3  6  7]      7
//  

// 提示：

// 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

