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
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {

}




func main() {
	l11 := list.BuildList([]int{1,2,4})
	l21 := list.BuildList([]int{1,3,4})
	

}



// 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

// 示例1：
// 输入：1->2->4, 1->3->4
// 输出：1->1->2->3->4->4

// 限制：
// 0 <= 链表长度 <= 1000

