#include <iostream>
using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if (s1.size() + s2.size() != s3.size())
            return false;

        bool dp[s1.size()+1][s2.size()+1];

        // 注意在dp中ij是长度，在s中是下标，要减1
        for (int i = 0; i <= s1.size(); ++i) {
            for (int j = 0; j <= s2.size(); ++j) {
                if (i == 0 && j == 0)
                    dp[i][j] = true;
                else if (i == 0)
                    dp[0][j] = dp[0][j-1] && s2[j-1] == s3[j-1];
                else if (j == 0)
                    dp[i][0] = dp[i-1][0] && s1[i-1] == s3[i-1];
                else
                    // 即s1或s2中有一个能把s3匹配掉，且之前也是交错的，那么新的也就交错
                    dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1]) || (dp[i][j-1] && s2[j-1] == s3[i+j-1]);
            }
        }
        return dp[s1.size()][s2.size()];
    }
};

void test(string test_name, string s1, string s2, string s3, bool expected)
{
    bool res = Solution().isInterleave(s1, s2, s3);
    if (res == expected)
        cout << test_name + " success." << endl;
    else
        cout << test_name + " failed." << endl;
}


int main()
{
    string s11 = "aabcc", s21 = "dbbca", s31 = "aadbbcbcac";
    bool expected1 = true;
    test("test1", s11, s21, s31, expected1);

    string s12 = "aabcc", s22 = "dbbca", s32 = "aadbbbaccc";
    bool expected2 = false;
    test("test2", s12, s22, s32, expected2);

    return 0;
}
