## 思路1 直接用切片反转

先记录正负号，直接用切片反转，然后用`int(str())`的方法去掉0。最后返回时判断一下有没有越界。


```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        res = sign * int(str(sign * x)[::-1])
        return 0 if res > 2 ** 31 -1 or res < -(2 ** 31) else res
```

## 思路2 用c++中的`long long`类型

用求模运算依次取得每一位，然后反转。注意负数求模会保留符号，如 -13 % 10 = -3。严格来讲这样做是不符合题目要求的，因为我们用到的longlong是64位。

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