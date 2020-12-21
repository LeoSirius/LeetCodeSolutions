package main

import (
	"fmt"
	"slt/util_go/list"
)

type ListNode = list.ListNode


func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	preHead := &ListNode{}
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

func test(testName string, l1, l2, expected *ListNode) {
	res := mergeTwoLists(l1, l2)
	if list.IsEqualList(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
	l11 := list.BuildList([]int{1,2,4})
	l21 := list.BuildList([]int{1,3,4})
	expected1 := list.BuildList([]int{1,1,2,3,4,4})
	test("test1", l11, l21, expected1)

}



// 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

// 示例1：
// 输入：1->2->4, 1->3->4
// 输出：1->1->2->3->4->4

// 限制：
// 0 <= 链表长度 <= 1000

