#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        
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
