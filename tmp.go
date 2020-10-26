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

func reverse(row []int) []int {
	size := len(row)
	for i, j := 0, size-1; i < j; i, j = i+1, j-1 {
		row[i], row[j] = row[j], row[i]
	}
	return row
}

func levelOrder(root *TreeNode) [][]int {
	res := [][]int{}
	if root == nil {
		return res
	}

	que := []*TreeNode{root}
	depth := 0
	for len(que) > 0 {
		curLevelSize := len(que)
		row := []int{}
		depth++
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
		if depth % 2 == 1 {
			res = append(res, row)
		} else {
			res = append(res, reverse(row))
		}
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
