#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        int res = 0;
        if (!s.size())
            return res;

        int start = 0;

        stack<int> left_stk;

        for (int i = 0; s[i]; i++) {
            if (s[i] == '(') {
                left_stk.push(i);
            } else {
                if (left_stk.empty()) {
                    start = i + 1;       // 右括号，且栈空，当前的这个右括号也要跳过。
                } else {
                    left_stk.pop();
                    if (left_stk.empty()) {
                        // (()) i = 3, start = 0, res = 4
                        res = max(res, i - start + 1);
                    } else {
                        // (())  i = 2, stack.top() = 0, res = 2, 即中间两个的长度
                        res = max(res, i - left_stk.top());
                    }
                }
            }
        }
        return res;
    }
};


void test(string test_name, string s, int expected)
{
    int res = Solution().longestValidParentheses(s);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "(()";
    int expected1 = 2;
    test("test1", s1, expected1);

    string s2 = ")()())";
    int expected2 = 4;
    test("test2", s2, expected2);
    return 0;
}
