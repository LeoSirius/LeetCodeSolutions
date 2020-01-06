#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        string res = "";
        vector<vector<bool>> dp(s.size(), vector<bool>(s.size(), false));
        for (int l = s.size() - 1; l >= 0; l--) {
            for (int r = l; r < s.size(); r++) {
                dp[l][r] = s[l] == s[r] && (r-l <= 2 || dp[l+1][r-1]);
                if (dp[l][r] && r-l+1 > res.size())
                    res = s.substr(l, r-l+1);
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

    string s3 = "a";
    vector<string> expected3 = {"a"};
    test("test3", s3, expected3);

    return 0;
}
