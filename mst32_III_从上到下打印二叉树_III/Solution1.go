package main

import (
	"slt/util_go/tree"
	"fmt"
	"reflect"
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
	var res [][]int
	var que []*TreeNode

	if root == nil {
		return res
	}

	que = append(que, root)
	depth := 1
	for len(que) > 0 {
		curLevelSize := len(que)
		var row []int
		for i := 0; i < curLevelSize; i++ {
			p := que[0]
			row = append(row, p.Val)
			que = que[1:]
			if p.Left != nil {
				que = append(que, p.Left)
			}
			if p.Right != nil {
				que = append(que, p.Right)
			}
		}

		if depth % 2 == 0 {
			for i, j := 0, len(row)-1; i < j; i, j = i+1, j-1 {
				row[i], row[j] = row[j], row[i]
			}
		}
		depth++
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
	root1 := &TreeNode{Val:3}
	root1.Left = &TreeNode{Val:9}
	root1.Right = &TreeNode{Val:20}
	root1.Right.Left = &TreeNode{Val:15}
	root1.Right.Right = &TreeNode{Val:7}
	expected1 := [][]int{
		{3},
		{20, 9},
		{15, 7}}
	test("test1", root1, expected1)
	
	//            0
	//        2      4
	//      1      3  -1
	//    5  1      6   8
	root2 := &TreeNode{Val:0}
	root2.Left = &TreeNode{Val:2}
	root2.Left.Left = &TreeNode{Val:1}
	root2.Left.Left.Left = &TreeNode{Val:5}
	root2.Left.Left.Right = &TreeNode{Val:1}
	root2.Right = &TreeNode{Val:4}
	root2.Right.Left = &TreeNode{Val:3}
	root2.Right.Left.Right = &TreeNode{Val:6}
	root2.Right.Right = &TreeNode{Val:-1}
	root2.Right.Right.Right = &TreeNode{Val:8}
	expected2 := [][]int{
		{0},
		{4,2},
		{1,3,-1},
		{8,6,1,5}}
	test("test2", root2, expected2)
}