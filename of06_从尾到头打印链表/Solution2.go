package main

import (
	"fmt"
	"reflect"
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
func reversePrint(head *ListNode) []int {
	res := []int{}

	var dfs func(*ListNode)
	dfs = func(node *ListNode) {
		if node == nil {
			return
		}
		dfs(node.Next)
		res = append(res, node.Val)
	}
	dfs(head)

	return res
}

func test(testName string, head *ListNode, expected []int) {
	res := reversePrint(head)
	if reflect.DeepEqual(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	head1 := list.BuildList([]int{1,3,2})
	expected1 := []int{2,3,1}
	test("test1", head1, expected1)

}


// 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

// 示例 1：

// 输入：head = [1,3,2]
// 输出：[2,3,1]