class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min_stk = []


    def push(self, x: int) -> None:
        self.stk.append(x)

        if (not self.min_stk) or (x <= self.min_stk[-1]):
            self.min_stk.append(x)

    def pop(self) -> None:
        if not self.stk:
            return

        tmp = self.stk.pop()
        if self.min_stk and tmp == self.min_stk[-1]:
            self.min_stk.pop()

    def top(self) -> int:
        if not self.stk:
            return 0
        return self.stk[-1]


    def getMin(self) -> int:
        if not self.min_stk:
            return 0
        return self.min_stk[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

def test1():
    stk = MinStack()
    stk.push(-2);
    stk.push(0);
    stk.push(-3);
    res1 = stk.getMin();    # -3
    stk.pop();
    res2 = stk.top();       # 0
    res3 = stk.getMin();    # -2
    if res1 == -3 and res2 == 0 and res3 == -2:
        print('test1 success.')
    else:
        print('test1 failed.')


def test2():
    stk = MinStack();
    stk.push(0);
    stk.push(1);
    stk.push(0);
    res1 = stk.getMin();    # 0
    stk.pop();
    res2 = stk.getMin();    # 0

    if res1 == 0 and res2 == 0:
        print('test2 success.')
    else:
        print('test2 failed.')

def test3():
    stk = MinStack()
    stk.push(2)
    stk.push(0)
    stk.push(3)
    stk.push(0)
    res1 = stk.getMin()     # 0
    stk.pop()
    res2 = stk.getMin()     # 0
    stk.pop()
    res3 = stk.getMin()     # 0
    stk.pop()
    res4 = stk.getMin()     # 2
    if (res1, res2, res3, res4) == (0, 0, 0, 2):
        print('test3 success.')
    else:
        print('test3 failed.')


if __name__ == "__main__":
    test1()
    test2()
    test3()

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
#  

# 提示：

# 各函数的调用总次数不超过 20000 次
#  

# 注意：本题与主站 155 题相同
