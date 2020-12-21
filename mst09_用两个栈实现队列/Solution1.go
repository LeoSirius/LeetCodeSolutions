package main

import (
	"fmt"
	"reflect"
)

type CQueue struct {
	si []int
	so []int
}


func Constructor() CQueue {
	return CQueue{}
}


func (this *CQueue) AppendTail(value int)  {
	this.si = append(this.si, value)
}


func (this *CQueue) DeleteHead() int {
	if len(this.so) == 0 {
		if len(this.si) == 0 {
			return -1
		}
		for len(this.si) > 0 {
			tmp := this.si[len(this.si)-1]
			this.si = this.si[:len(this.si)-1]
			this.so = append(this.so, tmp)
		}
	}
	res := this.so[len(this.so)-1]
	this.so = this.so[:len(this.so)-1]
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
