#include <iostream>
#include <stack>
using namespace std;

class MyQueue {
    stack<int> stk1, stk2;
public:
    /** Initialize your data structure here. */
    MyQueue() {

    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        stk1.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (stk2.empty()) {
            while (!stk1.empty()) {
                int tmp = stk1.top(); stk1.pop();
                stk2.push(tmp);
            }
        }
        int res = stk2.top(); stk2.pop();
        return res;
    }
    
    /** Get the front element. */
    int peek() {
        if (stk2.empty()) {
            while (!stk1.empty()) {
                int tmp = stk1.top(); stk1.pop();
                stk2.push(tmp);
            }
        }
        int res = stk2.top();
        return res;
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return stk1.empty() && stk2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */

void test1()
{
    MyQueue *que = new MyQueue();
    que->push(1);
    que->push(2);
    int res1 = que->peek();    // 1
    int res2 = que->pop();     // 1
    bool res3 = que->empty();  // false
    if (res1 == 1 && res2 == 1 && res3 == false)
        cout << "test1 success." << endl;
    else
        cout << "test1 failed." << endl;

}

int main()
{
    test1();

    return 0;
}



// Implement the following operations of a queue using stacks.

// push(x) -- Push element x to the back of queue.
// pop() -- Removes the element from in front of queue.
// peek() -- Get the front element.
// empty() -- Return whether the queue is empty.
// Example:

// MyQueue queue = new MyQueue();

// queue.push(1);
// queue.push(2);  
// queue.peek();  // returns 1
// queue.pop();   // returns 1
// queue.empty(); // returns false
// Notes:

// You must use only standard operations of a stack --
// which means only push to top, peek/pop from top, size, 
// and is empty operations are valid.
// Depending on your language, stack may not be supported natively.
// You may simulate a stack by using a list or deque (double-ended queue),
// as long as you use only standard operations of a stack.
// You may assume that all operations are valid (for example,
// no pop or peek operations will be called on an empty queue).
