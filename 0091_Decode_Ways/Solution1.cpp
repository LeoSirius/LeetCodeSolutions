#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int numDecodings(string s) {
        if (s.empty()) return 0;
        vector<int> dp (s.size() + 1, 0);
        dp[0] = 1;
        dp[1] = s[0] == '0' ? 0 : 1;
        for (int i = 2; i <= s.size(); i++) {
            int first = stoi(s.substr(i - 1, 1));
            int second = stoi(s.substr(i - 2, 2));
            if (first >= 1 && first <= 9) {
                dp[i] += dp[i-1];
            }
            if (second >= 10 && second <= 26) {
                dp[i] += dp[i-2];
            }
        }
        return dp[s.size()];
    }
};

void test(string test_name, string s, int expected)
{
    Solution slt;
    if (slt.numDecodings(s) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "12";
    int expected1 = 2;
    test("test1", s1, expected1);

    string s2 = "226";
    int expected2 = 3;
    test("test2", s2, expected2);

    string s3 = "12345";
    int expected3 = 3;
    test("test3", s3, expected3);

    return 0;
}
