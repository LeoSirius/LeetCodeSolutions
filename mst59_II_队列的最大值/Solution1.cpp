#include <iostream>
#include <queue>
#include <deque>
using namespace std;

class MaxQueue {
    queue<int> que;
    deque<int> deq;

public:
    MaxQueue() {
        while (!que.empty()) que.pop();
        while (!deq.empty()) deq.pop_back();
    }
    
    int max_value() {
        if (que.empty())
            return -1;
        return deq.front();
    }
    
    void push_back(int value) {
        que.push(value);

        if (deq.empty())
            deq.push_back(value);
        else {
            // 保证新插入的数比deq最后的数小，deq是从头到尾递减的
            while (!deq.empty() && deq.back() < value) {
                deq.pop_back();
            }
            deq.push_back(value);
        }
    }
    
    int pop_front() {
        if (que.empty())
            return -1;
        int res = que.front(); que.pop();
        if (res == deq.front())
            deq.pop_front();
        return res;
    }
};

void test1()
{
    MaxQueue mq = MaxQueue();
    mq.push_back(1);
    mq.push_back(2);
    int res1 = mq.max_value();
    int res2 = mq.pop_front();
    int res3 = mq.max_value();

    if (res1 == 2 && res2 == 1 && res3 == 2)
        cout << "test1 success." << endl;
    else
        cout << "test2 failed." << endl;
}

void test2()
{
    MaxQueue mq = MaxQueue();
    mq.pop_front();
    mq.pop_front();
    mq.pop_front();
    mq.pop_front();
    mq.pop_front();
    mq.push_back(15);
    int res1 = mq.max_value();
    mq.push_back(9);
    int res2 = mq.max_value();

    if (res1 == 15 && res2 == 15)
        cout << "test2 success." << endl;
    else
        cout << "test2 failed." << endl;

}

int main()
{
    test1();
    test2();
    return 0;
}




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

