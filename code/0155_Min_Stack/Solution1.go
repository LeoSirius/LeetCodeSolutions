package main

import (
	"fmt"
	"reflect"
)


type MinStack struct {
	stk []int
	mstk []int
}


/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{}
}


func (this *MinStack) Push(x int)  {
	this.stk = append(this.stk, x)
	if len(this.mstk) == 0 || x <= this.mstk[len(this.mstk)-1] {
		this.mstk = append(this.mstk, x)
	}
}


func (this *MinStack) Pop()  {
	if len(this.stk) == 0 {
		return
	}
	popValue := this.stk[len(this.stk)-1]
	this.stk = this.stk[:len(this.stk)-1]

	if len(this.mstk) > 0 && this.mstk[len(this.mstk)-1] == popValue {
		this.mstk = this.mstk[:len(this.mstk)-1]
	}
}


func (this *MinStack) Top() int {
	if len(this.stk) == 0 {
		return -1
	}
	return this.stk[len(this.stk)-1]
}


func (this *MinStack) Min() int {
	if len(this.mstk) == 0 {
		return -1
	}
	return this.mstk[len(this.mstk)-1]
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

