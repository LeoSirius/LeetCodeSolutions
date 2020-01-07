#include <iostream>
using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        
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

    return 0;
}
