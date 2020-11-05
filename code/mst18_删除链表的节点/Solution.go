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
func deleteNode(head *ListNode, val int) *ListNode {
	preHead := &ListNode{Next: head}
	p := preHead

	for p.Next != nil {
		if p.Next.Val == val {
			p.Next = p.Next.Next
			break
		}
		p = p.Next
	}
	return preHead.Next
}

func test(testName string, head *ListNode, val int, expected *ListNode) {
	res := deleteNode(head, val)
	if list.IsEqualList(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	head1 := list.BuildList([]int{4,5,1,9})
	val1 := 5
	expected1 := list.BuildList([]int{4,1,9})
	test("test1", head1, val1, expected1)

	head2 := list.BuildList([]int{4,5,1,9})
	val2 := 1
	expected2 := list.BuildList([]int{4,5,9})
	test("test2", head2, val2, expected2)

}


// 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

// 返回删除后的链表的头节点。

// 注意：此题对比原题有改动

// 说明：

// 题目保证链表中节点的值互不相同
// 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

// 示例 1:

// 输入: head = [4,5,1,9], val = 5
// 输出: [4,1,9]
// 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.


// 示例 2:

// 输入: head = [4,5,1,9], val = 1
// 输出: [4,5,9]
// 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
//  

// 说明：

// 题目保证链表中节点的值互不相同
// 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点
