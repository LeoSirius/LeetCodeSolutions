#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
    int operate(int a, int b, string operand)
    {
        if (operand == "+")
            return a + b;
        else if (operand == "-")
            return a - b;
        else if (operand == "*")
            return a * b;
        else
            return a / b;
    }
    
public:
    int evalRPN(vector<string>& tokens) {
        int res = 0;
        stack<int> stk;
        for (int i = 0; i < tokens.size(); i++) {
            string cur_str = tokens[i];
            if (cur_str == "+" || cur_str == "-" || cur_str == "*" || cur_str == "/") {
                // 注意后面的数先出栈
                int b = stk.top(); stk.pop();
                int a = stk.top(); stk.pop();
                int res = operate(a, b, tokens[i]);
                stk.push(res);
            } else {
                int num = stoi(tokens[i]);
                stk.push(num);
            }
        }
        return stk.top();
    }
};

void test(string test_name, vector<string>& tokens, int expected)
{
    int res = Solution().evalRPN(tokens);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<string> tokens1 = {"2", "1", "+", "3", "*"};
    int expected1 = 9;
    test("test1", tokens1, expected1);

    vector<string> tokens2 = {"4", "13", "5", "/", "+"};
    int expected2 = 6;
    test("test2", tokens2, expected2);

    vector<string> tokens3 = {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
    int expected3 = 22;
    test("test3", tokens3, expected3);

    return 0;
}

// Evaluate the value of an arithmetic expression in Reverse Polish Notation.

// Valid operators are +, -, *, /. 
// Each operand may be an integer or another expression.

// Note:

// Division between two integers should truncate toward zero.
// The given RPN expression is always valid. 
// That means the expression would always evaluate to a result and
// there won't' be any divide by zero operation.
// Example 1:

// Input: ["2", "1", "+", "3", "*"]
// Output: 9
// Explanation: ((2 + 1) * 3) = 9
// Example 2:

// Input: ["4", "13", "5", "/", "+"]
// Output: 6
// Explanation: (4 + (13 / 5)) = 6
// Example 3:

// Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
// Output: 22
// Explanation: 
//   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
// = ((10 * (6 / (12 * -11))) + 17) + 5
// = ((10 * (6 / -132)) + 17) + 5
// = ((10 * 0) + 17) + 5
// = (0 + 17) + 5
// = 17 + 5
// = 22

