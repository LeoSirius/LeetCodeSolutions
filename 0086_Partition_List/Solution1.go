package main

import (
	"fmt"
	"slt/util_go/list"
)

type ListNode = list.ListNode

func partition(head *ListNode, x int) *ListNode {
	p1, p2 := &ListNode{}, &ListNode{}
	
	h1 := p1
	h2 := p2
	p := head
	for p != nil {
		if p.Val >= x {
			p2.Next = p
			p2 = p2.Next
		} else {
			p1.Next = p
			p1 = p1.Next
		}
		p = p.Next
	}
	p1.Next = h2.Next
	p2.Next = nil
	return h1.Next
}

func test(testName string, head *ListNode, x int, expected *ListNode) {
	res := partition(head, x)
	if list.IsEqualList(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	head1 := list.BuildList([]int{1,4,3,2,5,2})
	x1 := 3
	expected1 := list.BuildList([]int{1,2,2,4,3,5})
	test("test1", head1, x1, expected1)

}
