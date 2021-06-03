### 思路1 常规数学转换 + 溢出检查

2^31-1 = 2147483647
-2^31 = -2147483648

在每次循环中，res都会乘以10，我们提前检查res和`INT_MIN/10, INT_MAX/10`的关系

如果res恰好等于`INT_MIN/10, INT_MAX/10`，则判断pop与7和-8的关系

注意 python 负数的整除和求模都和 c++ 不同

### 思路2 直接用切片反转（python是不会溢出的）（only python）

先记录正负号，直接用切片反转，然后用`int(str())`的方法去掉0。最后返回时判断一下有没有越界。


```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        res = sign * int(str(sign * x)[::-1])
        return 0 if res > 2 ** 31 -1 or res < -(2 ** 31) else res
```
