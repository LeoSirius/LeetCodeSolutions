#include <iostream>
#include <queue>
using namespace std;

class MyStack {
    queue<int> que;
public:
    /** Initialize your data structure here. */
    MyStack() {

    }
    
    /** Push element x onto stack. */
    void push(int x) {
        int size = que.size();
        que.push(x);
        while (size--) {
            int tmp = que.front(); que.pop();
            que.push(tmp);
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int res = que.front(); que.pop();
        return res;
    }
    
    /** Get the top element. */
    int top() {
        return que.front();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return que.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */

void test1()
{
    MyStack *obj = new MyStack();
    obj->push(1);
    obj->push(2);
    int res1 = obj->top();    // 2
    int res2 = obj->pop();    // 2
    bool res3 = obj->empty(); // false
    if (res1 == 2 && res2 == 2 && res3 == false)
        cout << "test1 success." << endl;
    else
        cout << "test1 failed." << endl;
}

int main()
{
    test1();
    return 0;
}

// Implement the following operations of a stack using queues.

// push(x) -- Push element x onto stack.
// pop() -- Removes the element on top of the stack.
// top() -- Get the top element.
// empty() -- Return whether the stack is empty.
// Example:

// MyStack stack = new MyStack();

// stack.push(1);
// stack.push(2);  
// stack.top();   // returns 2
// stack.pop();   // returns 2
// stack.empty(); // returns false
// Notes:

// You must use only standard operations of a queue -- 
// which means only push to back, peek/pop from front, size, 
// and is empty operations are valid.

// Depending on your language, queue may not be supported natively.
// You may simulate a queue by using a list or deque (double-ended queue),
// as long as you use only standard operations of a queue.

// You may assume that all operations are valid (for example, 
// no pop or top operations will be called on an empty stack).
