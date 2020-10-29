package main

import (
	"fmt"
	"reflect"
)

type MinStack struct {
	s []int
	smin []int
}

/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(x int)  {
	this.s = append(this.s, x)
	if len(this.smin) == 0 || x <= this.smin[len(this.smin)-1] {
		this.smin = append(this.smin, x)
	}
}


func (this *MinStack) Pop() {
	top := this.s[len(this.s)-1]
	if top == this.smin[len(this.smin)-1] {
		this.smin = this.smin[:len(this.smin)-1]
	}
	this.s = this.s[:len(this.s)-1]
}

func (this *MinStack) Top() int {
	return this.s[len(this.s)-1]

}

func (this *MinStack) Min() int {
	return this.smin[len(this.smin)-1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Min();
 */

func test1() {
	stk := Constructor()
	stk.Push(-2)
	stk.Push(0)
	stk.Push(-3)
	res1 := stk.Min()   // -3
	stk.Pop()
	res2 := stk.Top()   // 0
	res3 := stk.Min()   // -2
	
	a := []int{res1, res2, res3}
	b := []int{-3, 0, -2}
	if reflect.DeepEqual(a, b) {
		fmt.Println("test1 success.")
	} else {
		fmt.Println("test1 failed.")
	}
}

func test2() {
	stk := Constructor()
	stk.Push(0)
	stk.Push(1)
	stk.Push(0)
	res1 := stk.Min()      // 0
	stk.Pop()
	res2 := stk.Min()      // 0

	a := []int{res1, res2}
	b := []int{0, 0}
	if reflect.DeepEqual(a, b) {
		fmt.Println("test2 success.")
	} else {
		fmt.Println("test2 failed.")
	}
}

func main() {
	test1()
	test2()
}


// 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
// 调用 min、push 及 pop 的时间复杂度都是 O(1)。

// 示例:
// MinStack minStack = new MinStack();
// minStack.push(-2);
// minStack.push(0);
// minStack.push(-3);
// minStack.min();   --> 返回 -3.
// minStack.pop();
// minStack.top();      --> 返回 0.
// minStack.min();   --> 返回 -2.
//  

// 提示：

// 各函数的调用总次数不超过 20000 次
//  

// 注意：本题与主站 155 题相同

