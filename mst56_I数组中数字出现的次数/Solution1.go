package main

import (
    "fmt"
    "reflect"
)

func singleNumbers(nums []int) []int {
    allXor := 0
    for _, v := range(nums) {
        allXor ^= v
    }

    numFromRight := 1
    for allXor & 1 == 0 {
        numFromRight++
        allXor >>= 1
    }

    r1, r2 := 0, 0
    for _, v := range(nums) {
        if ((v >> (numFromRight-1)) & 1 == 0) {
            r1 ^= v
        } else {
            r2 ^= v
        }
    }

    return []int{r1, r2}
}

func test(testName string, nums []int, expected [][]int) {
    res := singleNumbers(nums)
    for _, v := range(expected) {
        if reflect.DeepEqual(res, v) {
            fmt.Println(testName + " success.")
            return
        }
    }
    fmt.Println(testName + " failed.")
}

func main() {
    nums1 := []int{4,1,4,6}
    expected1 := [][]int{{1,6}, {6,1}}
    test("test1", nums1, expected1)

    nums2 := []int{1,2,10,4,1,4,3,3}
    expected2 := [][]int{{2, 10}, {10, 2}}
    test("test2", nums2, expected2)
}


//  一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
//  要求时间复杂度是O(n)，空间复杂度是O(1)。

//  示例 1：
//  输入：nums = [4,1,4,6]
//  输出：[1,6] 或 [6,1]

//  示例 2：
//  输入：nums = [1,2,10,4,1,4,3,3]
//  输出：[2,10] 或 [10,2]

//  限制：
//  2 <= nums.length <= 10000
