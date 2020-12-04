package main

import (
	"fmt"
	"container/heap"
)

type IntHeap []int

func (h IntHeap) Len() int { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push (x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	target := old[n-1]
	*h = old[0:n-1]
	return target
}

func isPossible(nums []int) bool {
	chains := make(map[int]*IntHeap)
	// 这里没有用Python的default dict，所以写起来很复杂

	for _, n := range(nums) {
		curChain := chains[n]
		if chainOfLast, ok := chains[n-1]; !ok {
			
			if curChain == nil {
				curChain = &IntHeap{1}
				chains[n] = curChain
			} else {
				heap.Push(curChain, 1)
			}
		} else {
			minLenEndWithN := 0
			if len(*chainOfLast) >= 1 {
				minLenEndWithN = heap.Pop(chainOfLast).(int)
			}
			
			if curChain == nil {
				curChain = &IntHeap{minLenEndWithN + 1}
				chains[n] = curChain
			} else {
				heap.Push(curChain, minLenEndWithN + 1)
			}
		}
	}

	for _, h := range(chains) {
		if len(*h) > 0 && (*h)[0] < 3 {
			return false
		}
	}
	return true
}

func test(testName string, nums []int, expected bool) {
	res := isPossible(nums)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	nums1 := []int{1,2,3,3,4,5}
	expected1 := true
	test("test1", nums1, expected1)

	nums2 := []int{1,2,3,3,4,4,5,5}
	expected2 := true
	test("test2", nums2, expected2)

	nums3 := []int{1,2,3,4,4,5}
	expected3 := false
	test("test3", nums3, expected3)

	nums4 := []int{1,2,3,3}
	expected4 := false
	test("test4", nums4, expected4)
}



// nums1 = [1,2,3,3,4,5]
// expected1 = True
// test('test1', nums1, expected1)

// nums2 = [1,2,3,3,4,4,5,5]
// expected2 = True
// test('test2', nums2, expected2)

// nums3 = [1,2,3,4,4,5]
// expected3 = False
// test('test3', nums3, expected3)

// nums4 = [1,2,3,3]
// expected4 = False
// test('test4', nums4, expected4)


// 给你一个按升序排序的整数数组 num（可能包含重复数字），
// 请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。

// 如果可以完成上述分割，则返回 true ；否则，返回 false 。

//  

// 示例 1：

// 输入: [1,2,3,3,4,5]
// 输出: True
// 解释:
// 你可以分割出这样两个连续子序列 : 
// 1, 2, 3
// 3, 4, 5
//  

// 示例 2：

// 输入: [1,2,3,3,4,4,5,5]
// 输出: True
// 解释:
// 你可以分割出这样两个连续子序列 : 
// 1, 2, 3, 4, 5
// 3, 4, 5
//  

// 示例 3：

// 输入: [1,2,3,4,4,5]
// 输出: False
//  

// 提示：

// 输入的数组长度范围为 [1, 10000]

