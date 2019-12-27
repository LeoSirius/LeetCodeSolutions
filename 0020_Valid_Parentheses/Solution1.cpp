#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (char c : s) {
            switch(c) {
                case '(': stk.push(')'); break;
                case '[': stk.push(']'); break;
                case '{': stk.push('}'); break;
                default:
                    if (stk.empty() || stk.top() != c)
                        return false;
                    stk.pop();
            }
        }
        return stk.empty();
    }
};

void test(string test_name, string s, bool expected)
{
    Solution slt;
    if (slt.isValid(s) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "()";
    bool expected1 = true;
    test("test1", s1, expected1);

    string s2 = "()[]{}";
    bool expected2 = true;
    test("test2", s2, expected2);

    string s3 = "(]";
    bool expected3 = false;
    test("test3", s3, expected3);

    string s4 = "([)]";
    bool expected4 = false;
    test("test4", s4, expected4);

    string s5 = "{[]}";
    bool expected5 = true;
    test("test5", s5, expected5);

    return 0;
}
