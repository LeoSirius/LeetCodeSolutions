#include <iostream>
#include <vector>
using namespace std;

class Solution {
    vector<string> res;
    void back_track(string str, int l, int r)
    {
        if (!l && !r) {
            res.push_back(str);
            return;
        }
        // 注意这里必须判断一下，如果l或r已经是0，就不用加了
        if (l) back_track(str + "(", l-1, r+1);
        if (r) back_track(str + ")", l, r-1);
    }
public:
    vector<string> generateParenthesis(int n) {
        if (!n)
            return res;
        back_track("", n, 0);
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