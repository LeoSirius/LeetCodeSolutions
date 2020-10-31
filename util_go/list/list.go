package list

import "fmt"

type ListNode struct {
	Val int
	Next *ListNode
}

func BuildList(s []int) *ListNode {
	preHead := &ListNode{}
	p := preHead
	for _, v := range s {
		p.Next = &ListNode{Val: v}
		p = p.Next
	}
	return preHead.Next
}

func PrintList(l *ListNode) {
	p := l
	for p != nil {
		fmt.Printf("%v, ", p.Val)
		p = p.Next
	}
	fmt.Println()
}

func IsEqualList(l1, l2 *ListNode) bool {
	if l1 == nil && l2 == nil {
		return true
	}
	if l1 == nil || l2 == nil {
		return false
	}
	if l1.Val != l2.Val {
		return false
	}
	return IsEqualList(l1.Next, l2.Next)
}
