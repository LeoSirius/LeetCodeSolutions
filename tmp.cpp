#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size()+1, false);
        dp[0] = true;
        unordered_set<string> ms(wordDict.begin(), wordDict.end());

        for (int i = 1; i <= s.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && ms.find(s.substr(j, i-j)) != ms.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.size()];
    }
};

void test(string test_name, string s, vector<string> &wordDict, bool expected)
{
    if (Solution().wordBreak(s, wordDict) == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string s1 = "leetcode";
    vector<string> wordDict1 = {
        "leet", "code"
    };
    bool expected1 = true;
    test("test1", s1, wordDict1, expected1);

    string s2 = "applepenapple";
    vector<string> wordDict2 = {
        "apple", "pen"
    };
    bool expected2 = true;
    test("test2", s2, wordDict2, expected2);

    string s3 = "catsandog";
    vector<string> wordDict3 = {
        "cats", "dog", "sand", "and", "cat"
    };
    bool expected3 = false;
    test("test3", s3, wordDict3, expected3);

    return 0;
}