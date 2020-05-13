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

