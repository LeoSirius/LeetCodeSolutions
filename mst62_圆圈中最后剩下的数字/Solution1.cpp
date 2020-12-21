#include <iostream>
using namespace std;

class Solution {
public:
    int lastRemaining(int n, int m) {
        if (n == 1)
            return 0;
        int x = lastRemaining(n-1, m);
        return (m + x) % n;
    }
};

void test(string test_name, int n, int m, int expected)
{
    int res = Solution().lastRemaining(n, m);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 5, m1 = 3;
    int expected1 = 3;
    test("test1", n1, m1, expected1);

    int n2 = 10, m2 = 17;
    int expected2 = 2;
    test("test2", n2, m2, expected2);

    return 0;
}


// 0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。
// 求出这个圆圈里剩下的最后一个数字。

// 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，
// 则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

//  

// 示例 1：

// 输入: n = 5, m = 3
// 输出: 3
// 示例 2：

// 输入: n = 10, m = 17
// 输出: 2
//  

// 限制：

// 1 <= n <= 10^5
// 1 <= m <= 10^6
