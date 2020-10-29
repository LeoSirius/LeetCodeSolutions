class MaxQueue:

    def __init__(self):
        self.que = []
        self.deq = []


    def max_value(self) -> int:
        if not self.deq:
            return -1
        return self.deq[0]


    def push_back(self, value: int) -> None:
        self.que.append(value)

        if not self.deq:
            self.deq.append(value)
            return
        
        while self.deq and self.deq[-1] < value:
            self.deq = self.deq[:-1]
        self.deq.append(value)

    def pop_front(self) -> int:
        if not self.que:
            return -1
        front = self.que[0]
        self.que = self.que[1:]

        if self.deq and front == self.deq[0]:
            self.deq = self.deq[1:]

        return front



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()


def test1():
    mq = MaxQueue()
    mq.push_back(1)
    mq.push_back(2)
    res1 = mq.max_value()    # 2
    res2 = mq.pop_front()    # 1
    res3 = mq.max_value()    # 2

    if (res1, res2, res3) == (2,1,2):
        print('test1 success.')
    else:
        print('test1 failed.')


def test2():
    mq = MaxQueue()
    mq.pop_front()
    mq.pop_front()
    mq.pop_front()
    mq.pop_front()
    mq.pop_front()
    mq.push_back(15)
    res1 = mq.max_value()    # 15
    mq.push_back(9)
    res2 = mq.max_value()    # 15

    if (res1, res2) == (15, 15):
        print('test2 success.')
    else:
        print('test2 failed.')


def test3():
    mq = MaxQueue()
    res1 = mq.max_value()    # -1
    res2 = mq.pop_front()    # -1
    res3 = mq.pop_front()    # -1
    mq.push_back(94)
    mq.push_back(16)
    mq.push_back(89)
    res4 = mq.pop_front()    # 94
    mq.push_back(22)
    res5 = mq.pop_front()    # 16

    if (res1, res2, res3, res4, res5) == (-1, -1, -1, 94, 16):
        print('test3 success.')
    else:
        print('test3 failed.')

# 140 837 545

# ["MaxQueue",""""p,"","push_back","push_back","pop_front","push_back","push_back","push_back","push_back","pop_front","max_value","push_back","max_value","max_value","pop_front","max_value","max_value","max_value","push_back","pop_front","push_back","pop_front","max_value","max_value","max_value","push_back","pop_front","push_back","push_back","push_back","pop_front","max_value","pop_front","max_value","max_value","max_value","pop_front","push_back","pop_front","push_back","push_back","pop_front","push_back","pop_front","push_back","pop_front","pop_front","push_back","pop_front","pop_front","pop_front","push_back","push_back","max_value","push_back","pop_front","push_back","push_back","pop_front"]
# [[],[],[],[],[46],[],[],[],[],[868],[],[],[],[525],[],[],[],[],[123],[646],[],[229],[],[],[],[871],[],[],[285],[],[],[],[],[45],[140],[837],[545],[],[],[],[],[],[],[561],[237],[],[633],[98],[806],[717],[],[],[186],[],[],[],[],[],[],[268],[],[29],[],[],[],[],[866],[],[239],[3],[850],[],[],[],[],[],[],[],[310],[],[674],[770],[],[525],[],[425],[],[],[720],[],[],[],[373],[411],[],[831],[],[765],[701],[]]

# [null,-1,-1,-1,null,46,46,-1,-1,null,868,-1,-1,null,525,-1,-1,-1,null,null,646,null,646,646,646,null,123,871,null,871,871,871,646,null,null,null,null,229,871,646,285,45,646,null,null,140,null,null,null,null,837,806,null,806,806,545,806,806,806,null,561,null,237,806,806,806,null,633,null,null,null,98,866,806,866,866,866,717,null,186,null,null,268,null,29,null,866,239,null,3,850,310,null,null,806,null,674,null,null,770]

# [null,-1,-1,-1,null,46,46,-1,-1,null,868,-1,-1,null,525,-1,-1,-1,null,null,646,null,646,646,646,null,123,871,null,871,871,871,646,null,null,null,null,229,871,837,285,45,837,null,null,140,null,null,null,null,837,806,null,806,806,545,806,806,806,null,561,null,237,806,806,806,null,633,null,null,null,98,866,806,866,866,866,717,null,186,null,null,268,null,29,null,866,239,null,3,850,310,null,null,770,null,674,null,null,770]

if __name__ == "__main__":
    test1()
    test2()
    test3()


# 请定义一个队列并实现函数 max_value 得到队列里的最大值，
# 要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

# 若队列为空，pop_front 和 max_value 需要返回 -1

# 示例 1：

# 输入: 
# ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
# [[],[1],[2],[],[],[]]
# 输出: [null,null,null,2,1,2]
# 示例 2：

# 输入: 
# ["MaxQueue","pop_front","max_value"]
# [[],[],[]]
# 输出: [null,-1,-1]
#  

# 限制：

# 1 <= push_back,pop_front,max_value的总操作数 <= 10000
# 1 <= value <= 10^5
