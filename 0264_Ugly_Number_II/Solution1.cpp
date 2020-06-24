#include <iostream>
using namespace std;

class Solution {
public:
    int nthUglyNumber(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        int p2 = 0, p3 = 0, p5 = 0;

        int dp[n];
        dp[0] = 1;
        for (int i = 1; i < n; i++) {
            dp[i] = min(min(dp[p2]*2, dp[p3]*3), dp[p5]*5);

            // 注意这里不能是 else if，就算上面的min不是由对应的p235生成的，p235也需要++，不然会有重复的
            if (dp[i] == dp[p2]*2) ++p2;
            if (dp[i] == dp[p3]*3) ++p3;
            if (dp[i] == dp[p5]*5) ++p5;
        }
        return dp[n-1];
    }
};

void test(string test_name, int n, int expected)
{
    int res = Solution().nthUglyNumber(n);
    cout << "res = " << res << endl;
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }

}

int main()
{
    int n1 = 10;
    int expected1 = 12;
    test("test1", n1, expected1);

    return 0;
}
