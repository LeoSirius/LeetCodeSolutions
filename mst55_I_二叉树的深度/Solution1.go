package main

import (
	"slt/util_go/tree"
	"fmt"
	"math"
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
func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	lDepth, rDepth := maxDepth(root.Left), maxDepth(root.Right)
	return int(math.Max(float64(lDepth), float64(rDepth))) + 1
}

func test(testName string, root *TreeNode, expected int) {
	res := maxDepth(root)
	if res == expected {
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
	root1 := &TreeNode{Val:1}
	root1.Left = &TreeNode{Val:9}
	root1.Right = &TreeNode{Val:20}
	root1.Right.Left = &TreeNode{Val:15}
	root1.Right.Right = &TreeNode{Val:7}
	expected1 := 3
	test("test1", root1, expected1)
}

// 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

// 例如：

// 给定二叉树 [3,9,20,null,null,15,7]，

//     3
//    / \
//   9  20
//     /  \
//    15   7
// 返回它的最大深度 3 。

//  

// 提示：

// 节点总数 <= 10000