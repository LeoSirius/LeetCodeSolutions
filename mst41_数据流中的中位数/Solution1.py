from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = [] # 小顶堆，保存较大的一半，且小顶堆的元素个数可以多一个
        self.max_heap = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        # Python 中 heapq 模块是小顶堆。实现 大顶堆 方法： 小顶堆的插入和弹出操作均将元素 取反 即可。
        if len(self.min_heap) == len(self.max_heap):
            # 数量相等，放小顶堆
            heappush(self.max_heap, -num)
            heappush(self.min_heap, -heappop(self.max_heap))
        else:
            # 数量不等，必然是小顶堆多一个。放大顶堆
            heappush(self.min_heap, num)
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) != len(self.max_heap):
            return self.min_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2.0


def test1():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    res1 = mf.findMedian() # 1.5
    mf.addNum(3)
    res2 = mf.findMedian() # 2.0
    if (res1, res2) == (1.5, 2.0):
        print('test1 success.')
    else:
        print('test1 failed.')

def test2():
    mf = MedianFinder()
    mf.addNum(2)
    res1 = mf.findMedian()  # 2.0
    mf.addNum(3)
    res2 = mf.findMedian()  # 2.5
    if (res1, res2) == (2.0, 2.5):
        print('test2 success.')
    else:
        print('test2 failed.')

if __name__ == "__main__":
    test1()
    test2()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
# 那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
# 那么中位数就是所有数值排序之后中间两个数的平均值。

# 例如，

# [2,3,4] 的中位数是 3

# [2,3] 的中位数是 (2 + 3) / 2 = 2.5

# 设计一个支持以下两种操作的数据结构：

# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。

# 示例 1：
# 输入：
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
# 输出：[null,null,null,1.50000,null,2.00000]

# 示例 2：
# 输入：
# ["MedianFinder","addNum","findMedian","addNum","findMedian"]
# [[],[2],[],[3],[]]
# 输出：[null,null,2.00000,null,2.50000]
#  

# 限制：
# 最多会对 addNum、findMedia进行 50000 次调用。
