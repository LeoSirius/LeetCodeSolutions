package tree

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func IsEqualTree(t1, t2 *TreeNode) bool {
	if t1 == nil && t2 == nil {
		return true
	}
	if t1 == nil || t2 == nil {
		return false
	}
	if t1.Val != t2.Val {
		return false
	}
	return IsEqualTree(t1.Left, t2.Left) && IsEqualTree(t1.Right, t2.Right)
}