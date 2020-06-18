#include <iostream>
#include <cmath>
#include <queue>
using namespace std;

class MedianFinder {
public:
    priority_queue<int, vector<int>, less<int>> max_que;    // 大顶堆，存放小的一半数
    priority_queue<int, vector<int>, greater<int>> min_que; // 小顶堆，存放大的一半数

    /** initialize your data structure here. */
    MedianFinder() {

    }
    
    void addNum(int num) {
        // 如果大小相等，放到大顶堆中。并平衡中间的数。其实是小顶推多一个
        if (max_que.size() == min_que.size()) {
            max_que.push(num);
            min_que.push(max_que.top()); max_que.pop();
        // 如果小顶堆多一个。则放到小顶堆中。并平衡中间的数。平衡到大顶堆。
        } else if (max_que.size() + 1 == min_que.size()) {
            min_que.push(num);
            max_que.push(min_que.top()); min_que.pop();
        }
    }
    
    double findMedian() {
        if (min_que.size() == max_que.size()) {
            return (min_que.top() + max_que.top()) / 2.0;
        }
        // add的时候是保持小顶堆多一个。所以如果数量不等。则中间的数就是大顶堆的top
        return double(min_que.top());
    }
};

void test1()
{
    MedianFinder *mf = new MedianFinder();
    mf->addNum(1);
    mf->addNum(2);
    double res1 = mf->findMedian();   // 1.50000
    mf->addNum(3);
    double res2 = mf->findMedian();   // 2.00000

    if (abs(double(res1 - 1.50000)) <= 0.000001 && abs(double(res2 - 2.00000)) <= 0.000001)
        cout << "test1 success." << endl;
    else
        cout << "test1 failed." << endl;
}

void test2()
{
    MedianFinder *mf = new MedianFinder();
    mf->addNum(2);
    double res1 = mf->findMedian();   // 2.00000
    mf->addNum(3);
    double res2 = mf->findMedian();   // 2.50000

    if (abs(double(res1 - 2.00000)) <= 0.000001 && abs(double(res2 - 2.50000)) <= 0.000001)
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
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

// 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
// 那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
// 那么中位数就是所有数值排序之后中间两个数的平均值。

// 例如，

// [2,3,4] 的中位数是 3

// [2,3] 的中位数是 (2 + 3) / 2 = 2.5

// 设计一个支持以下两种操作的数据结构：

// void addNum(int num) - 从数据流中添加一个整数到数据结构中。
// double findMedian() - 返回目前所有元素的中位数。
// 示例 1：

// 输入：
// ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
// [[],[1],[2],[],[3],[]]
// 输出：[null,null,null,1.50000,null,2.00000]


// 示例 2：
// 输入：
// ["MedianFinder","addNum","findMedian","addNum","findMedian"]
// [[],[2],[],[3],[]]
// 输出：[null,null,2.00000,null,2.50000]
//  

// 限制：
// 最多会对 addNum、findMedia进行 50000 次调用。

