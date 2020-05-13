#include <iostream>
using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        if (n == INT_MIN) {
            x *= x;
            n /= 2;
        }
        if (n < 0) {
            n = -n;     // 如果这里n=INT_MIN的话会溢出
            x = 1 / x;
        }
        return (n % 2 == 0) ? myPow(x * x, n / 2) : x * myPow(x * x, n / 2);
    }
};

void test(string test_name, double x, int n, double expected)
{
    Solution s;
    double res = s.myPow(x, n);
    if (-0.00001 < res - expected && res - expected < 0.00001) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    double x1 = 2;
    int n1 = 10;
    double expected1 = 1024;
    test("test1", x1, n1, expected1);

    double x2 = 2.1;
    int n2 = 3;
    double expected2 = 9.261;
    test("test2", x2, n2, expected2);

    double x3 = 2;
    int n3 = -2;
    double expected3 = 0.25;
    test("test3", x3, n3, expected3);

    double x4 = 2;
    int n4 = INT_MIN;
    double expected4 = 0;
    test("test4", x4, n4, expected4);

    return 0;
}
