#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) return 1;
        else if (n == 2) return 2;
        vector<int> dp(n, 1);
        dp[1] = 2;
        for (int i = 2; i < n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n-1];
    }
};

void test(string test_name, int n, int expected)
{
    Solution s;
    if (s.climbStairs(n) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 2;
    int expected1 = 2;
    // Explanation: There are two ways to climb to the top.
    // 1. 1 step + 1 step
    // 2. 2 steps
    test("test1", n1, expected1);

    int n2 = 3;
    int expected2 = 3;
    // Explanation: There are three ways to climb to the top.
    // 1. 1 step + 1 step + 1 step
    // 2. 1 step + 2 steps
    // 3. 2 steps + 1 step
    test("test2", n2, expected2);

    int n3 = 1;
    int expected3 = 1;
    test("test3", n3, expected3);

    return 0;
}
