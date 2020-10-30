#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minCut(string s) {
        int size = s.size();
        if (!size)
            return 0;
        vector<int> cut(size, 0);
        vector<vector<bool>> dp(size, vector<bool>(size, false));
        for (int i = size - 1; 0 <= i; --i) {
            cut[i] = size - 1 - i;  // 初始化 最右边的是0，和从左开始是镜像
            for (int j = i; j < size; ++j) {
                // 如果s[i,j]是回文
                if (s[i] == s[j] && (j - i < 2 || dp[i+1][j-1] == true)) {
                    dp[i][j] = true;
                    if (j == size - 1)
                        cut[i] = 0;   // j到了最后，说明整个s[i,j]都是回文
                    // s[i,j]是回文，切1次，再加上之前求的剩下s[j+1,n]
                    else
                        cut[i] = min(cut[i], 1 + cut[j+1]);
                }
            }
        }
        return cut[0];
    }
};

void test(string test_name, string s, int expected)
{
    int res = Solution().minCut(s);
    cout << "res = " << res << endl;
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string s1 = "aab";
    int expected1 = 1;
    test("test1", s1, expected1);

    return 0;
}