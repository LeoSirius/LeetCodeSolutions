class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        old_size = len(self.que)
        self.que.append(x)
        while old_size:
            self.que.append(self.que.pop(0))
            old_size -= 1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.que.pop(0)


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.que[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.que) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


def test1():
    stk = MyStack()
    stk.push(1)
    stk.push(2)
    res1 = stk.top()   # 2
    res2 = stk.pop()   # 2
    res3 = stk.empty() # False
    if res1 == 2 and res2 == 2 and res3 == False:
        print('test1 success.')
    else:
        print('test1 failed.')

if __name__ == '__main__':
    test1()

# Implement the following operations of a stack using queues.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Example:

# MyStack stack = new MyStack();

# stack.push(1);
# stack.push(2);  
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# Notes:

# You must use only standard operations of a queue -- 
# which means only push to back, peek/pop from front, size, 
# and is empty operations are valid.

# Depending on your language, queue may not be supported natively.
# You may simulate a queue by using a list or deque (double-ended queue),
# as long as you use only standard operations of a queue.

# You may assume that all operations are valid (for example, 
# no pop or top operations will be called on an empty stack).