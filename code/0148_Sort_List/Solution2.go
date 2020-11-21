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
func sortList(head *ListNode) *ListNode {

	if head == nil || head.Next == nil {
		return head
	}

	p1, p2 := head, head
	for p2 != nil && p2.Next != nil && p2.Next.Next != nil {
		p1 = p1.Next
		p2 = p2.Next.Next
	}
	tmp := p1.Next
	p1.Next = nil
	l1 := sortList(head)
	l2 := sortList(tmp)

	preHead := &ListNode{Next: head}
	p := preHead
	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			p.Next = l1
			l1 = l1.Next
		} else {
			p.Next = l2
			l2 = l2.Next
		}
		p = p.Next
	}
	if l1 != nil {
		p.Next = l1
	} else {
		p.Next = l2
	}
	return preHead.Next

}

func test(testName string, head, expected *ListNode) {
	res := sortList(head)
	if list.IsEqualList(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	head1 := list.BuildList([]int{4,2,1,3})
	expected1 := list.BuildList([]int{1,2,3,4})
	test("test1", head1, expected1)

	head2 := list.BuildList([]int{-1,5,3,4,0})
	expected2 := list.BuildList([]int{-1,0,3,4,5})
	test("test2", head2, expected2)

	head3 := list.BuildList([]int{})
	expected3 := list.BuildList([]int{})
	test("test3", head3, expected3)

	head4 := list.BuildList([]int{4,19,14,5,-3,1,8,5,11,15})
	expected4 := list.BuildList([]int{-3,1,4,5,5,8,11,14,15,19})
	test("test4", head4, expected4)

}

// Given the head of a linked list, return the list after sorting it in ascending order.

// Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

