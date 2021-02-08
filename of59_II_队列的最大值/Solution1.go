package main

import (
	"fmt"
	"reflect"
)

type MaxQueue struct {
	que []int
	deq []int
}


func Constructor() MaxQueue {
	return MaxQueue{}
}


func (this *MaxQueue) Max_value() int {
	if len(this.deq) == 0 {
		return -1
	}
	return this.deq[0]
}


func (this *MaxQueue) Push_back(value int)  {
	this.que = append(this.que, value)

	for len(this.deq) > 0 && this.deq[len(this.deq)-1] < value {
		this.deq = this.deq[:len(this.deq)-1]
	}
	this.deq = append(this.deq, value)
}


func (this *MaxQueue) Pop_front() int {
	if len(this.que) == 0 {
		return -1
	}

	res := this.que[0]
	this.que = this.que[1:]

	if len(this.deq) > 0 && res == this.deq[0] {
		this.deq = this.deq[1:]
	}
	return res
}


/**
 * Your MaxQueue object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Max_value();
 * obj.Push_back(value);
 * param_3 := obj.Pop_front();
 */


func test1() {
	mq := Constructor()
	mq.Push_back(1)
	mq.Push_back(2)
	res1 := mq.Max_value()    // 2
	res2 := mq.Pop_front()    // 1
	res3 := mq.Max_value()    // 2

	a := []int{res1, res2, res3}
	b := []int{2,1,2}
	if reflect.DeepEqual(a, b) {
		fmt.Println("test1 success.")
	} else {
		fmt.Println("test1 failed.")
	}
}

func test2() {
	mq := Constructor()
	mq.Pop_front()
	mq.Pop_front()
	mq.Pop_front()
	mq.Pop_front()
	mq.Pop_front()
	mq.Push_back(15)
	res1 := mq.Max_value()    // 15
	mq.Push_back(9)
	res2 := mq.Max_value()    // 15

	if res1 == 15 && res2 == 15 {
		fmt.Println("test2 success.")
	} else {
		fmt.Println("test2 failed.")
	}
}



func main() {
	test1()
	test2()
}

// 请定义一个队列并实现函数 max_value 得到队列里的最大值，
// 要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

// 若队列为空，pop_front 和 max_value 需要返回 -1

// 示例 1：

// 输入: 
// ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
// [[],[1],[2],[],[],[]]
// 输出: [null,null,null,2,1,2]
// 示例 2：

// 输入: 
// ["MaxQueue","pop_front","max_value"]
// [[],[],[]]
// 输出: [null,-1,-1]
//  

// 限制：

// 1 <= push_back,pop_front,max_value的总操作数 <= 10000
// 1 <= value <= 10^5
 