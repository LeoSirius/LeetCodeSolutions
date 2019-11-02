
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        // p 表示列号。对每一列，遍历所有字符串
        for (int p = 0; strs.size() > 0; prefix += strs[0][p++]) {
            for (int i = 0 ; i < strs.size(); i++) {
                // p已经走到了最短那个字符串的尽头 or
                // p列有字符不同， 则返回
                if (p >= strs[i].size() || (i > 0 && strs[i][p] != strs[i-1][p]))
                    return prefix;
            }
        }
        return prefix;
    }
};

void test(string test_name, vector<string>& strs, string exptectd)
{
    Solution s;
    if (s.longestCommonPrefix(strs) == exptectd) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{   
    vector<string> param1 = {"flower", "flow", "flight"};
    test("test1", param1, "fl");
    return 0;
}