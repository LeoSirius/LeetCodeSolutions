## 思路1 使用longlong

用求模运算依次取得每一位，然后反转。

注意负数求模会保留符号，如 -13 % 10 = -3

严格来讲这样做是不符合题目要求的，因为我们用到的longlong是64位。

```cpp
class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        while(x){
            res = res * 10 + x % 10;
            x /= 10;
        }
        return (res > INT_MAX || res < INT_MIN) ? 0 : res;
    }
};
```