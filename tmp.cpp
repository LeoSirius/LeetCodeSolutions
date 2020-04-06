#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int numDistinct(string s, string t) {
        vector<vector<long>> dp(s.size()+1, vector<long>(t.size()+1, 0));
        for (int i = 0; i <= s.size(); ++i) {
            for (int j = 0; j <= t.size(); ++j) {
                if (j == 0)
                    dp[i][0] = 1;
                else if (i && j) {
                    if (s[i-1] != t[j-1])
                        dp[i][j] = dp[i-1][j];
                    else {
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-1];
                    }
                }
            }
        }
        return dp.back().back();
    }
};

void test(string test_name, string s, string t, int expected)
{
    int res = Solution().numDistinct(s, t);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string s1 = "rabbbit", t1 = "rabbit";
    int expected1 = 3;
    test("test1", s1, t1, expected1);

    string s2 = "babgbag", t2 = "bag";
    int expected2 = 5;
    test("test2", s2, t2, expected2);

    return 0;
}
