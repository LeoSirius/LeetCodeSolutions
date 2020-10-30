#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
        for (int col = 0; strs.size() > 0; res += strs[0][col++]) {
            for (int row = 0; row < strs.size(); row++) {
                // col已经走到了最短那个字符串的尽头 or
                // col有字符不同， 则返回
                if (col >= strs[row].size() || row > 0 && strs[row][col] != strs[row-1][col])
                    return res;
            }
        }
        return res;
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
