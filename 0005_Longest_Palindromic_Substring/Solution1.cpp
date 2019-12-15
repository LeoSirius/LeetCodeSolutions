#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int len = s.size();
        string res = "";
        vector<vector<bool>> dp(len, vector<bool>(len, false));
        for (int l = len - 1; l >= 0; l--) {
            for (int r = l; r < len; r++) {
                dp[l][r] = s[l] == s[r] && (r - l <= 2 || dp[l+1][r-1]);
                if (dp[l][r] && r + 1 - l > res.size()) {
                    res = s.substr(l, r + 1 - l);
                }
            }
        }
        return res;
    }
};

void test(string test_name, string s, vector<string> expected)
{
    Solution slt;
    string res = slt.longestPalindrome(s);
    if (find(expected.begin(), expected.end(), res) != expected.end()) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "babad";
    vector<string> expected1 = {"bab", "aba"};
    test("test1", s1, expected1);

    string s2 = "cbbd";
    vector<string> expected2 = {"bb"};
    test("test2", s2, expected2);

    return 0;
}
