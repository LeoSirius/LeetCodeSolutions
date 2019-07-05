## 思路1 直接无脑转换

本质上还是hash的思想

```cpp
class Solution {
public:
    string intToRoman(int num) {
        string I[10] = {"", "I","II","III","IV","V","VI","VII","VIII","IX"};
        string X[10] = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        string C[10] = {"", "C", "CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        string M[4] = {"", "M","MM","MMM"};
        return M[num/1000]+C[num/100%10]+X[num/10%10]+I[num%10];
    }
};
```

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[(num%10)]
```