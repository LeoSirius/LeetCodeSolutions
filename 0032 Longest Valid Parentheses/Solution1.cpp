#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        if (s.empty())
            return 0;

        stack<int> stk; // 存放左括号的索引
        int one_before_start = -1;
        int max_len = 0;

        for (int i = 0; s[i]; ++i) {
            if (s[i] == '(') {
                stk.push(i);
            } else {
                if (stk.empty()) {         // 遇到右括号且栈空，则跳过，如))))))()
                    one_before_start = i;
                } else {
                    stk.pop();
                    // 弹完之后空，则从start开始算
                    // 弹完之后不空，则算当前栈顶的索引
                    if (stk.empty()) {
                        max_len = max(max_len, i - one_before_start); // (()) i = 3, one_before = -1, res = 4
                    } else {
                        max_len = max(max_len, i - stk.top());        // (())  i = 2, stack.top() = 0, res = 2, 即中间两个的长度
                    }
                }
            }
        }
        return max_len;
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
