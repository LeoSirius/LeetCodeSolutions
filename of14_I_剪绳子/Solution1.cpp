#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int cuttingRope(int n) {
        vector<int> dp(n + 1, 0);
        dp[0] = dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j < i; j++)
                dp[i] = max(dp[i], max(j * (i-j), j * dp[i-j]));
        }
        return dp.back();
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