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
func mirrorTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	left, right := mirrorTree(root.Left), mirrorTree(root.Right)
	root.Left, root.Right = right, left
	return root
}

func test(testName string, root, expected *TreeNode) {
	res := mirrorTree(root)
	if tree.IsEqualTree(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	//      4
	//    /   \
	//   2     7
	//  / \   / \
	// 1   3 6   9
	root1 := &TreeNode{Val:4}
	root1.Left = &TreeNode{Val:2}
	root1.Left.Left = &TreeNode{Val:1}
	root1.Left.Right = &TreeNode{Val:3}
	root1.Right = &TreeNode{Val:7}
	root1.Right.Left = &TreeNode{Val:6}
	root1.Right.Right = &TreeNode{Val:9}

	//      4
	//    /   \
	//   7     2
	//  / \   / \
	// 9   6 3   1
	expected1 := &TreeNode{Val:4}
	expected1.Left = &TreeNode{Val:7}
	expected1.Right = &TreeNode{Val:2}
	expected1.Left.Left = &TreeNode{Val:9}
	expected1.Left.Right = &TreeNode{Val:6}
	expected1.Right.Left = &TreeNode{Val:3}
	expected1.Right.Right = &TreeNode{Val:1}

	test("test1", root1, expected1)
}

// 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

// 例如输入：

//      4
//    /   \
//   2     7
//  / \   / \
// 1   3 6   9
// 镜像输出：

//      4
//    /   \
//   7     2
//  / \   / \
// 9   6 3   1

// 限制：
// 0 <= 节点个数 <= 1000