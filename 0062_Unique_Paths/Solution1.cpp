#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++)
                dp[j] += dp[j-1];
        }
        return dp[n-1];
    }
};

void test(string test_name, int m, int n, int expected)
{
    Solution s;
    if (s.uniquePaths(m, n) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int m1 = 3, n1 = 2, expected1 = 3;
    test("test1", m1, n1, expected1);

    int m2 = 7, n2 = 3, expected2 = 28;
    test("test2", m2, n2, expected2);

    return 0;
}