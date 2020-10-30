#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (char ch : s) {
            if (ch == '(' || ch == '[' || ch == '{')
                stk.push(ch);
            else {
                if (stk.empty()) return false;
                if (ch == ')') {
                    if (stk.top() != '(') return false;
                    stk.pop();
                } else if (ch == ']') {
                    if (stk.top() != '[') return false;
                    stk.pop();
                } else if (ch == '}') {
                    if (stk.top() != '{') return false;
                    stk.pop();
                }
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

// Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
//  determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Note that an empty string is also considered valid.
