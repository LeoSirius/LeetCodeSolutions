class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.mstk = []


    def push(self, x: int) -> None:
        self.stk.append(x)
        if not self.mstk or self.mstk[-1] >= x:
            self.mstk.append(x)


    def pop(self) -> None:
        res = self.stk.pop()
        if self.mstk and res == self.mstk[-1]:
            self.mstk.pop()


    def top(self) -> int:
        return self.stk[-1]


    def min(self) -> int:
        return self.mstk[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

def test1():
    mstk = MinStack()
    mstk.push(-2)
    mstk.push(0)
    mstk.push(-3)
    res1 = mstk.min()  # -3
    mstk.pop()
    res2 = mstk.top()  # 0
    res3 = mstk.min()  # -2

    if (res1, res2, res3) == (-3, 0, -2):
        print('test1 success.')
    else:
        print('test1 failed.')


if __name__ == "__main__":
    test1()


# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
# 调用 min、push 及 pop 的时间复杂度都是 O(1)。

# 示例:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.

# 提示：

# 各函数的调用总次数不超过 20000 次