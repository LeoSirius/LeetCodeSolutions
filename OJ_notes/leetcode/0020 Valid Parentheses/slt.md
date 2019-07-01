## 思路1 利用字典映射左右括号

注意括号交错要返回False

一种映射方法是只把右括号push入栈

```cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for(char&c : s){
            switch(c){
                case '[': stk.push(']'); break;
                case '(': stk.push(')'); break;
                case '{': stk.push('}'); break;
                default:
                    if(stk.size() == 0 || c != stk.top()) return false;
                    else stk.pop();
            }
        }
        return stk.empty();
    }
};
```

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mydict = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in mydict.values():
                stack.append(char)
            elif char in mydict.keys():
                if stack == [] or mydict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
```