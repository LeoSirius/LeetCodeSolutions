#include <iostream>
using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN) {
            if (divisor == 1)
                return INT_MIN;
            else if (divisor == -1)
                return INT_MAX;
            else {
                return ((divisor & 1) == 1) ? divide(dividend + 1, divisor) : divide(dividend >> 1, divisor >> 1);
            }
        }

        if (divisor == INT_MIN)
            return 0;
        
        int dvd = abs(dividend), dvs = abs(divisor), res = 0, x = 0;
        while (dvs <= dvd) {
            for (x = 0; (dvd /2 )- (dvs<<x) >= 0; x++);
            res += 1 << x;
            dvd -= dvs << x;
        }
        return (dividend > 0 == divisor > 0) ? res : -res;
    }
};


void test(string test_name, int dividend, int divisor, int expected)
{
    Solution s;
    if (s.divide(dividend, divisor) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int dividend1 = 10;
    int divisor1 = 3;
    int expected1 = 3;
    test("test1", dividend1, divisor1, expected1);

    int dividend2 = 7;
    int divisor2 = -3;
    int expected2 = -2;
    test("test2", dividend2, divisor2, expected2);

    int dividend3 = -1;
    int divisor3 = -1;
    int expected3 = 1;
    test("test3", dividend3, divisor3, expected3);

    int dividend4 = 2147483647;
    int divisor4 = 1;
    int expected4 = 2147483647;
    test("test4", dividend4, divisor4, expected4);

    int dividend5 = -2147483648;
    int divisor5 = 2;
    int expected5 = -1073741824;
    test("test5", dividend5, divisor5, expected5);

    return 0;
}