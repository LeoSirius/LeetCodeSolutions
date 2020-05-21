#include <iostream>
using namespace std;

class MaxQueue {
public:
    MaxQueue() {

    }

    int max_value() {

    }

    void push_back(int value) {

    }

    int pop_front() {

    }
};

void test1()
{
    
}

int main()
{


    return 0;
}

// 用一个queue和一个deque实现

// queue就是正常的que，负责push和pop
// deque用来存放最大值

// 如果新的value大于deque尾端的值，那么deque一直进行pop_back操作，
// 直到尾端的值大于等于value 或者为空
// 再将value压入deque的尾部

// 每次取max_value，返回deque首部的值

// 当que进行pop操作时，如果que首部的值等于deque首部的值，那么deque同样需要进行pop_front操作

// 总结完毕

/**
 * Your MaxQueue object will be instantiated and called as such:
 * MaxQueue* obj = new MaxQueue();
 * int param_1 = obj->max_value();
 * obj->push_back(value);
 * int param_3 = obj->pop_front();
 */

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

