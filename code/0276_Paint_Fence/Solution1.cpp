#include <iostream>
using namespace std;

class Solution {
public:
    int numWays(int n, int k) {
        if (n == 0 || k == 0) return 0;
        if (n == 1) return k;
        int dp[n+1];
        dp[1] = k;
        dp[2] = k * k;
        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) * (k-1);
        }
        return dp[n];
    }
};

void test(string test_name, int n, int k, int expected)
{
    if (Solution().numWays(n, k) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 3;
    int k1 = 2;
    int expected1 = 6;
    test("test1", n1, k1, expected1);

    int n2 = 1;
    int k2 = 1;
    int expected2 = 1;
    test("test2", n2, k2, expected2);

    return 0;
}
