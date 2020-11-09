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
func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	var a *ListNode
	b := head

	for b != nil {
		c := b.Next
		b.Next = a
		a, b = b, c
	}
	return a
}

func test(testName string, head, expected *ListNode) {
	res := reverseList(head)
	if list.IsEqualList(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	head1 := list.BuildList([]int{1,2,3,4,5})
	expected1 := list.BuildList([]int{5,4,3,2,1})
	test("test1", head1, expected1)

	head2 := list.BuildList([]int{})
	expected2 := list.BuildList([]int{})
	test("test2", head2, expected2)

}

// 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

// 示例:
// 输入: 1->2->3->4->5->NULL
// 输出: 5->4->3->2->1->NULL
//  

// 限制：
// 0 <= 节点个数 <= 5000

