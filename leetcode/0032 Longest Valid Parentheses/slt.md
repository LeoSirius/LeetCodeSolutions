### 思路1 利用一个栈来存放左括号的下标

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> stk;        // 存放左括号的下标
        int left_most = -1;    // left_most + 1 是当前匹配括号的开始索引
        int max_len = 0;
        for (int i = 0; s[i]; i++) {
            if (s[i] == '(') {
                stk.push(i);
            } else {
                if (stk.empty()) {
                    left_most = i;
                } else {
                    stk.pop();
                    if (stk.empty()) {
                        max_len = max(max_len, i - left_most);  // e.g. ))()  i = 3, leftmost = 1, res = 2
                    } else {
                        max_len = max(max_len, i - stk.top());  // e.g. (())  i = 2, stack.top() = 0, res = 2
                    }
                }
            }
        }
        return max_len;
    }
};
```

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