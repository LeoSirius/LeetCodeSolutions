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
func getKthFromEnd(head *ListNode, k int) *ListNode {
	fast, slow := head, head

	for i := 0; i < k; i++ {
		fast = fast.Next
	}

	for fast != nil {
		slow = slow.Next
		fast = fast.Next
	}
	return slow
}

func test(testName string, head *ListNode, k int, expected *ListNode) {
	res := getKthFromEnd(head, k)
	if list.IsEqualList(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	head1 := list.BuildList([]int{1,2,3,4,5})
	k1 := 2
	expected1 := list.BuildList([]int{4,5})
	test("test1", head1, k1, expected1)

	head2 := list.BuildList([]int{1})
	k2 := 1
	expected2 := list.BuildList([]int{1})
	test("test2", head2, k2, expected2)


}

// 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，
// 即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，
// 它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

// 示例：

// 给定一个链表: 1->2->3->4->5, 和 k = 2.
// 返回链表 4->5.
