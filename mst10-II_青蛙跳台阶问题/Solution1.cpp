#include <iostream>
using namespace std;

class Solution {
public:
    int numWays(int n) {
        int last2 = 1, last1 = 1;
        if (n == 0 || n == 1)
            return last1;
        for (int i = 2; i <= n; i++) {
            int tmp = last1;
            last1 = (last1 + last2) % 1000000007;
            last2 = tmp;
        }
        return last1;
    }
};
// 1000000007

void test(string test_name, int n, int expected)
{
    int res = Solution().numWays(n);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int n1 = 2;
    int expected1 = 2;
    test("test1", n1, expected1);

    int n2 = 7;
    int expected2 = 21;
    test("test2", n2, expected2);

    int n3 = 0;
    int expected3 = 1;
    test("test3", n3, expected3);
}
