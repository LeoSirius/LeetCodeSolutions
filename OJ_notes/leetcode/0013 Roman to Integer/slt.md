## 思路1 比后面小减当前，比后面大加当前

```cpp
class Solution {
public:
    int romanToInt(string s) {
        map<char, int> mapping = {
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000},
        };
        int res = 0;
        for(int i = 0; s[i+1]; ++i){
            if(mapping[s[i]] >= mapping[s[i+1]]){
                res += mapping[s[i]];
            }else{
                res -= mapping[s[i]];
            }
        }
        res += mapping[s[s.size()-1]];
        return res;
    }
};
```

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        for i in range(len(s) - 1):
            if mapping[s[i]] >= mapping[s[i+1]]:
                res += mapping[s[i]]
            else:
                res -= mapping[s[i]]
        return res + mapping[s[-1]]
```