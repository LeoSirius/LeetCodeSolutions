## 思路1 遍历字符串

按照题意，遇到第一个（非正负号 && 非空格 && 非数字）的字符就停止

```cpp
class Solution {
public:
    int myAtoi(string str) {
        long long result = 0;
        int indicator = 1;
        int i = str.find_first_not_of(' ');
        if(i == -1)         // in case of str = "    "
            return 0;

        if(str[i] == '-' || str[i] == '+')
            indicator = (str[i++] == '-') ? -1 : 1;
        
        while(str[i] >= '0' && str[i] <= '9'){
            result = result*10 + str[i++]-'0';
            cout << "result = " << result << endl; 
            if(result*indicator >= INT_MAX) return INT_MAX;
            if(result*indicator <= INT_MIN) return INT_MIN;
        }
        return result*indicator;
    }
};
```

最后判断是否越界时用`min`与最大数比，用`max`与最小数比。`cpp`中不能这样用，因为`min`、`max`两个参数的类型要求一样

```python
class Solution:
    def myAtoi(self, str: str) -> int:
        ls = list(str.strip())
        if len(ls) == 0:
            return 0
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+'] : del ls[0]
        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            res = res * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign*res, 2**31-1))
```