package main

import (
	"fmt"
	"reflect"
	"slt/util_go/tree"
)

type TreeNode = tree.TreeNode

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
	res := [][]int{}
	if root == nil {
		return res
	}

	que := []*TreeNode{root}
	for len(que) > 0 {
		curLevelSize := len(que)
		row := []int{}
		for i := 0; i < curLevelSize; i++ {
			p := que[0]
			que = que[1:]
			row = append(row, p.Val)
			if p.Left != nil {
				que = append(que, p.Left)
			}
			if p.Right != nil {
				que = append(que, p.Right)
			}
		}
		res = append(res, row)
	}
	return res
}


func test(testName string, root *TreeNode, expected [][]int) {
	res := levelOrder(root)
	if reflect.DeepEqual(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	//     3
	//    / \
	//   9  20
	//     /  \
	//    15   7
	root1 := &TreeNode{Val: 3}
	root1.Left = &TreeNode{Val: 9}
	root1.Right = &TreeNode{Val: 20}
	root1.Right.Left = &TreeNode{Val: 15}
	root1.Right.Right = &TreeNode{Val: 7}
	expected1 := [][]int{
		{3},
		{9, 20},
		{15, 7}}
	test("test1", root1, expected1)
}
