package main

import (
	"fmt"
)

func maxSubArray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	dp := make([]int, len(nums))
	for i := range dp {
		dp[i] = 0
	}
	dp[0] = nums[0]

	for i := 1; i < len(nums); i++ {
		// 如果前一次小于0，则这里相当于重置
		if dp[i-1] < 0 {
			dp[i] = nums[i]
		} else {
			dp[i] = dp[i-1] + nums[i]
		}
	}

	// 最后获取dp中的最大值
	res := dp[0]
	for i := 1; i < len(dp); i++ {
		if dp[i] > res {
			res = dp[i]
		}
	}
	return res
}

func test(testName string, nums []int, expected int) {
	res := maxSubArray(nums)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	nums1 := []int{-2,1,-3,4,-1,2,1,-5,4}
	expected1 := 6
	test("test1", nums1, expected1)

	nums2 := []int{-2, -1}
	expected2 := -1
	test("test2", nums2, expected2)

}


// 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

// 要求时间复杂度为O(n)。

// 示例1:

// 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
// 输出: 6
// 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
//  

// 提示：

// 1 <= arr.length <= 10^5
// -100 <= arr[i] <= 100

