package main

import (
	"fmt"
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

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	var isSym func(l, r *TreeNode) bool

	isSym = func(l, r *TreeNode) bool {
		if l == nil && r == nil {
			return true
		}
		if l == nil || r == nil {
			return false
		}
		if l.Val != r.Val {
			return false
		}
		return isSym(l.Left, r.Right) && isSym(l.Right, r.Left)
	}
	return isSym(root.Left, root.Right)
}

func test(testName string, root *TreeNode, expected bool) {
	res := isSymmetric(root)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	//     1
	//    / \
	//   2   2
	//  / \ / \
	// 3  4 4  3
	root1 := &tree.TreeNode{Val: 1}
	root1.Left = &tree.TreeNode{Val: 2}
	root1.Left.Left = &tree.TreeNode{Val: 3}
	root1.Left.Right = &tree.TreeNode{Val: 4}
	root1.Right = &tree.TreeNode{Val: 2}
	root1.Right.Left = &tree.TreeNode{Val: 4}
	root1.Right.Right = &tree.TreeNode{Val: 3}
	expected1 := true
	test("test1", root1, expected1)

	//     1
	//    / \
	//   2   2
	//    \   \
	//    3    3
	root2 := &tree.TreeNode{Val: 1}
	root2.Left = &tree.TreeNode{Val: 2}
	root2.Left.Right = &tree.TreeNode{Val: 3}
	root2.Right = &tree.TreeNode{Val: 2}
	root2.Right.Right = &tree.TreeNode{Val: 3}
	expected2 := false
	test("test2", root2, expected2)

	// nil
	var root3 *TreeNode
	expected3 := true
	test("test3", root3, expected3)
}