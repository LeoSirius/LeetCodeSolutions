## 思路1 把除法转化为减法

题目明确不能用乘、除、模运算，我们只使用加减法和位移运算。temp只会是divisor的2、4、8...倍，每当dividend减去i倍的divisor，就往结果里加i

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            i_times_of_divisor, i = divisor, 1
            while dividend >= i_times_of_divisor:
                dividend -= i_times_of_divisor
                res += i
                i <<= 1
                i_times_of_divisor <<= 1
        if not positive:
            res = -res
        return min(max(res, -2**31), 2**31-1)
```