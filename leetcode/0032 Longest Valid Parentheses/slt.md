### 思路1 利用一个栈来存放左括号的下标

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) < 2:
            return 0
        stack = []
        leftmost = -1 # point to index one before match substr
        res = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else: # c == ')'
                if not stack:  
                    #  not match, update leftmost to i
                    leftmost = i
                else:
                    stack.pop()
                    if not stack:
                        # e.g. ))()  i = 3, leftmost = 1, res = 2
                        res = max(res, i - leftmost)
                    else:
                        # e.g. (())  i = 2, stack[-1] = 0, res = 2
                        res = max(res, i - stack[-1])
        return res
```