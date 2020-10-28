package main

import (
	"fmt"
	"reflect"
)

type CQueue struct {
	sI []int
	sO []int
}


func Constructor() CQueue {
	return CQueue{}
}


func (this *CQueue) AppendTail(value int)  {
	this.sI = append(this.sI, value)
}


func (this *CQueue) DeleteHead() int {
	if len(this.sI) == 0 && len(this.sO) == 0 {
		return -1
	}
	if len(this.sO) > 0 {
		res := this.sO[len(this.sO)-1]
		this.sO = this.sO[:len(this.sO)-1]
		return res
	}

	for len(this.sI) > 0 {
		topAtIn := this.sI[len(this.sI)-1]
		this.sI = this.sI[:len(this.sI)-1]
		this.sO = append(this.sO, topAtIn)
	}

	res := this.sO[len(this.sO)-1]
	this.sO = this.sO[:len(this.sO)-1]
	return res
}


/**
 * Your CQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AppendTail(value);
 * param_2 := obj.DeleteHead();
 */

func test1() {
	q := Constructor()
	q.AppendTail(3)
	res1 := q.DeleteHead()
	res2 := q.DeleteHead()

	a := []int{res1, res2}
	b := []int{3, -1}
	if reflect.DeepEqual(a, b) {
		fmt.Println("test1 success.")
	} else {
		fmt.Println("test1 failed.")
	}
}


func main() {
	test1()
}
