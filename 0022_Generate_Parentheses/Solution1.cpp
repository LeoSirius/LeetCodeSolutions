#include <iostream>
#include <vector>
using namespace std;

class Solution {
    void dfs(int l, int r, vector<string> &res, string str)
    {
        if (l == 0 && r == 0) {
            res.push_back(str);
            return;
        }
        if (l) dfs(l-1, r+1, res, str+"(");
        if (r) dfs(l, r-1, res, str+")");
    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if (n == 0) {
            return res;
        }
        dfs(n, 0, res, "");
        return res;
    }
};

void test(string test_name, int n, vector<string> expected)
{
    Solution s;
    vector<string> res = s.generateParenthesis(n);
    sort(res.begin(), res.end());
    sort(expected.begin(), expected.end());
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 3;
    vector<string> expected1 = {
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    };
    test("test1", n1, expected1);

    return 0;
}
