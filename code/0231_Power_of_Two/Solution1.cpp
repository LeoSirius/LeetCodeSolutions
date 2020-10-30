#include <iostream>
using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        int power_of2 = 1;
        while (power_of2 <= n) {
            if (power_of2 == n) return true;
            if (power_of2 > INT_MAX / 2) break;  // 防止溢出
            power_of2 *= 2;
        }
        return false;
    }
};

void test(string test_name, int n, bool expected)
{
    Solution s;
    bool res = s.isPowerOfTwo(n);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 1;
    bool expected1 = true;
    test("test1", n1, expected1);

    int n2 = 16;
    bool expected2 = true;
    test("test2", n2, expected2);

    int n3 = 218;
    bool expected3 = false;
    test("test3", n3, expected3);

    int n4 = 1073741825;
    bool expected4 = false;
    test("test4", n4, expected4);

    return 0;
}
