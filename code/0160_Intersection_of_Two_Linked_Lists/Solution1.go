package main

import (
	"fmt"
	"slt/util_go/list"
)

type ListNode = list.ListNode

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	p1, p2 := headA, headB
	for p1 != p2 {
		if p1 != nil {
			p1 = p1.Next
		} else {
			p1 = headB
		}
		if p2 != nil {
			p2 = p2.Next
		} else {
			p2 = headA
		}
	}
	return p1
}

func test(testName string, headA, headB, expected *ListNode) {
	res := getIntersectionNode(headA, headB)
	if list.IsEqualList(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	// 输入：intersectVal = 8,
	// listA = [4,1,8,4,5],
	// listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
	// 输出：Reference of the node with value = 8
	headA1 := list.BuildList([]int{4,1,8,4,5})
	headB1 := list.BuildList([]int{5,0,1})
	headB1.Next.Next.Next = headA1.Next.Next
	expected1 := list.BuildList([]int{8,4,5})
	test("test1", headA1, headB1, expected1)

	headA2 := list.BuildList([]int{2,6,4})
	headB2 := list.BuildList([]int{1,5})
	var expected2 *ListNode
	test("test2", headA2, headB2, expected2)

}


// 如果两个链表没有交点，返回 null.
// 在返回结果后，两个链表仍须保持原有的结构。
// 可假定整个链表结构中没有循环。
// 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。


