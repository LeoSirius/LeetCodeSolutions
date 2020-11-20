package main

import (
	"fmt"
	
	"slt/util_go/list"
)

type ListNode = list.ListNode;

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func insertionSortList(head *ListNode) *ListNode {
	preHead := &ListNode{}

	cur := head
	for cur != nil {
		p := preHead

		for p.Next != nil && p.Next.Val < cur.Val {
			p = p.Next
		}

		tmp := cur.Next
		
		cur.Next = p.Next
		p.Next = cur

		cur = tmp
	}
	return preHead.Next
	
}

func test(testName string, head, expected *ListNode) {
	res := insertionSortList(head)
	if list.IsEqualList(res, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
	head1 := list.BuildList([]int{4,2,1,3})
	expected1 := list.BuildList([]int{1,2,3,4})
	test("test1", head1, expected1)

	head2 := list.BuildList([]int{-1,5,3,4,0})
	expected2 := list.BuildList([]int{-1, 0, 3, 4, 5})
	test("test2", head2, expected2)

}

// A graphical example of insertion sort. 
// The partial sorted list (black) initially contains only the first 
// element in the list.
// With each iteration one element (red) is removed from the 
// input data and inserted in-place into the sorted list
//  

// Algorithm of Insertion Sort:

// Insertion sort iterates, consuming one input element each repetition, 
// and growing a sorted output list.
// At each iteration, insertion sort removes one element from the input data,
// finds the location it belongs within the sorted list, and inserts it there.
// It repeats until no input elements remain.

// Example 1:

// Input: 4->2->1->3
// Output: 1->2->3->4

// Example 2:

// Input: -1->5->3->4->0
// Output: -1->0->3->4->5

