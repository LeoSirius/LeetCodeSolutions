#include <iostream>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && pop > 7)) return 0;
            if (res < INT_MIN / 10 || (res == INT_MIN / 10 && pop < -8)) return 0;
            res = res * 10 + pop;
        }
        return res;
    }
};

void test(string test_name, int x, int expected)
{
    Solution s;
    if (s.reverse(x) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int x1 = 123;
    int expected1 = 321;
    test("test1", x1, expected1);

    int x2 = -123;
    int expected2 = -321;
    test("test2", x2, expected2);

    int x3 = 120;
    int expected3 = 21;
    test("test3", x3, expected3);

    return 0;
}
