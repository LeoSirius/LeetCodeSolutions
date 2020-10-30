#include <iostream>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        if (x == 1) return 1;
        int l = 0, r = x;
        // 即l = r - 1的时候停止。
        while (l < r - 1) {
            // 最后l*l < x, r*r > x
            int mid = l + (r - l) / 2;
            if (mid > x / mid) {
                r = mid;
            } else {
                l = mid;
            }
        }
        return l;
    }
};

void test(string test_name, int x, int expected)
{
    Solution s;
    int res = s.mySqrt(x);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int x1 = 4;
    int expected1 = 2;
    test("test1", x1, expected1);

    int x2 = 8;
    int expected2 = 2;
    test("test2", x2, expected2);

    int x3 = 2147395600;
    int expected3 = 46340;
    test("test3", x3, expected3);

    return 0;
}
