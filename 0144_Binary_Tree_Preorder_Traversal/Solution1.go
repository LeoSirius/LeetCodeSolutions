package main

import (
	"fmt"
	"slt/util_go/tree"
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
func preorderTraversal(root *TreeNode) []int {
	res := []int{}
	if root == nil {
		return res
	}

	stk := []*TreeNode{}
	p := root
	for len(stk) > 0 || p != nil {
		for p != nil {
			stk = append(stk, p)
			res = append(res, p.Val)
			p = p.Left
		}
		p = stk[len(stk)-1]
		stk = stk[:len(stk)-1]
		p = p.Right
	}
	return res
}


func test(testName string, root *TreeNode, expected []int) {
	res := preorderTraversal(root)
	fmt.Printf("res = %v\n", res)
	if reflect.DeepEqual(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
    //  1
    //   \
    //    2
    //   /
	//  3
	root1 := &TreeNode{Val: 1}
	root1.Right = &TreeNode{Val:2}
	root1.Right.Left = &TreeNode{Val: 3}
	expected1 := []int{1,2,3}
	test("test1", root1, expected1)

	root2 := &TreeNode{Val: 1}
	root2.Left = &TreeNode{Val: 2}
	expected2 := []int{1, 2}
	test("test2", root2, expected2)
}