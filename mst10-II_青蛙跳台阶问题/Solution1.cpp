#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int numWays(int n) {
        if (n == 0)
            return 1;
        else if (n == 1)
            return 1;
        else if (n == 2)
            return 2;

        vector<int> dp(n + 1, 0);
        dp[1] = 1; dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i] + dp[i-1] + dp[i-2]) % 1000000007;
        }
        return dp.back();
    }
};

void test(string test_name, int n, int expected)
{
    int res = Solution().numWays(n);
    cout << res << endl;
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