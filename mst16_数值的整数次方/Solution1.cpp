#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0)
            return 1;
        if (n == INT_MIN) {
            n /= 2;
            x *= x;
        }
        if (n < 0) {
            n = -n;
            x = 1/x;
        }
        return n % 2 == 0 ? myPow(x * x, n / 2) : x * myPow(x * x, n / 2);
    }
};

void test(string test_name, double x, int n, double expected)
{
    double res = Solution().myPow(x, n);
    cout << "res = " << res << endl;
    if (abs(res - expected) < 0.00001)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    double x1 = 2;
    int n1 = 10;
    double expected1 = 1024;
    test("test1", x1, n1, expected1);

    double x2 = 2.1;
    int n2 = 3;
    double expected2 = 9.26100;
    test("test2", x2, n2, expected2);

    double x3 = 2;
    int n3 = -2;
    double expected3 = 0.25000;
    test("test3", x3, n3, expected3);

    double x4 = 0.44528;
    int n4 = 0;
    double expected4 = 1;
    test("test4", x4, n4, expected4);

    return 0;
}


// 实现函数double Power(double base, int exponent)，求base的exponent次方。
// 不得使用库函数，同时不需要考虑大数问题。


// 示例 1:
// 输入: 2.00000, 10
// 输出: 1024.00000

// 示例 2:
// 输入: 2.10000, 3
// 输出: 9.26100

// 示例 3:
// 输入: 2.00000, -2
// 输出: 0.25000
// 解释: 2-2 = 1/22 = 1/4 = 0.25

// 说明:

// -100.0 < x < 100.0
// n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
// 注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/
