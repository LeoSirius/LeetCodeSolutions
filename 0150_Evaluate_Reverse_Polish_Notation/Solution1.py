from typing import *
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b, a = stk.pop(), stk.pop()
                if token == '+':
                    stk.append(a+b)
                elif token == '-':
                    stk.append(a-b)
                elif token == '*':
                    stk.append(a*b)
                else:
                    # 這裡是 python 複數整除的一個坑，10 // -3 = -4
                    # 複數除不盡的應該是向上取整，但是 python 中複數也是向下
                    stk.append(math.trunc(a/b))
            else:
                stk.append(int(token))

        return int(stk[0])


def test(test_name, tokens, expected):
    res = Solution().evalRPN(tokens)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    tokens1 = ["2", "1", "+", "3", "*"]
    expected1 = 9;
    test('test1', tokens1, expected1)

    tokens2 = ["4", "13", "5", "/", "+"]
    expected2 = 6;
    test('test2', tokens2, expected2)

    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    expected3 = 22;
    test('test3', tokens3, expected3)

    tokens4 = ["2","1","+","3","*"]
    expected4 = 9
    test('test4', tokens4, expected4)

    tokens5 = ["4","-2","/","2","-3","-","-"]
    expected5 = -7
    test('test5', tokens5, expected5)


# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. 
# Each operand may be an integer or another expression.

# Note:

# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. 
# That means the expression would always evaluate to a result and
# there won't' be any divide by zero operation.
# Example 1:

# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
