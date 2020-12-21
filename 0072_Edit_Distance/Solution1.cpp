#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.size() + 1, vector<int>(word2.size() + 1, 0));

        for (int i = 0; i <= word1.size(); ++i)
            dp[i][0] = i;
        for (int j = 0; j <= word2.size(); ++j)
            dp[0][j] = j;

        for (int i = 1; i < dp.size(); i++) {
            for (int j = 1; j < dp[0].size(); j++) {
                if (word1[i-1] == word2[j-1])    // 注意dp的i和j在word中是从1开始表示的，dp[i][j]的原意就是前i和j个字符转换完成
                    dp[i][j] = dp[i-1][j-1];
                else {
                    dp[i][j] = min(min(dp[i-1][j-1], dp[i][j-1]), dp[i-1][j]) + 1;
                }
            }
        }
        return dp.back().back();
    }
};

void test(string test_name, string word1, string word2, int expected)
{
    int res = Solution().minDistance(word1, word2);
    cout << "res = " << res << endl;
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string word11 = "horse";
    string word21 = "ros";
    int expected1 = 3;
    test("test1", word11, word21, expected1);


    string word12 = "intention", word22 = "execution";
    int expected2 = 5;
    test("test2", word12, word22, expected2);
    return 0;
}