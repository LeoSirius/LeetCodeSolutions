#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    int cuttingRope(int n) {
        if (n < 4)      // n = 2, 3
            return n-1;
        int a = n / 3, b = n % 3;
        if (b == 0)
            return pow(3, a);
        if (b == 1)
            return pow(3, a-1) * 4;
        if (b == 2)
            return pow(3, a) * 2;
        return 0;                   // impossible, for compile
    }
};

void test(string test_name, int n, int expected)
{
    int res = Solution().cuttingRope(n);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int n1 = 2;
    int expected1 = 1;
    test("test1", n1, expected1);

    int n2 = 10;
    int expected2 = 36;
    test("test2", n2, expected2);

    return 0;
}
