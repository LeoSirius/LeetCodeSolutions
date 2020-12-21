#include <iostream>
#include <stack>
using namespace std;

class MinStack {
    stack<int> stk;
    stack<int> mstk;
    int minval;
public:
    /** initialize your data structure here. */
    MinStack() {
        while (!stk.empty()) stk.pop();
        while (!mstk.empty()) mstk.pop();
    }
    
    void push(int x) {
        stk.push(x);
        if (mstk.empty() || x <= mstk.top())
            mstk.push(x);
    }
    
    void pop() {
        int res = stk.top(); stk.pop();
        if (!mstk.empty() && res == mstk.top())
            mstk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return mstk.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->min();
 */

void test1()
{
    MinStack stk = MinStack();
    stk.push(-2);
    stk.push(0);
    stk.push(-3);
    int res1 = stk.getMin();    // -3
    stk.pop();
    int res2 = stk.top();    // 0
    int res3 = stk.getMin();    // -2
    if (res1 == -3 && res2 == 0 && res3 == -2)
        cout << "test1 success." << endl;
    else
        cout << "test1 failed." << endl;
}

void test2()
{
    MinStack stk = MinStack();
    stk.push(0);
    stk.push(1);
    stk.push(0);
    int res1 = stk.getMin();   // 0
    stk.pop();
    int res2 = stk.getMin();   // 0

    if (res1 == 0 && res2 == 0)
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

