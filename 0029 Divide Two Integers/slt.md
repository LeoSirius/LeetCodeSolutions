## 思路1 把除法转化为减法

题目明确不能用乘、除、模运算，我们只使用加减法和位移运算。temp只会是divisor的2、4、8...倍，每当dividend减去i倍的divisor，就往结果里加i。

INT_MAX 定义为2**32 - 1， 也就是2147483647。INT_MIN不能直接定义为-2147483648，因为这是一个表达式，是2147483648取负数。这样写已经溢出。INT_MIN定义为(-INT_MAX)-1。cpp中一开始把可能溢出的case考虑了。python在最后考虑。其实这道题可能溢出的就只有一种情况， 即dividend=-2147483648，而divisor=-1。

temp也要用long，因为在内部的while中，测试条件是temp左移后和dvd比较。

temp增长：temp * 2, temp * 4, temp * 8...
m增长：2, 4, 8...

```cpp
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
        long dvd = labs(dividend), dvs = labs(divisor), ans = 0;
        int sign = dividend > 0 ^ divisor > 0 ? -1 : 1;
        while (dvd >= dvs) {
            long temp = dvs, m = 1;
            while (temp << 1 <= dvd) {
                temp <<= 1;
                m <<= 1;
            }
            dvd -= temp;
            ans += m;
        }
        return sign * ans;
    }
};
```

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            i_times_of_divisor, i = divisor, 1
            while dividend >= i_times_of_divisor:
                dividend -= i_times_of_divisor
                res += i
                i <<= 1     # 左移以为相当于乘2
                i_times_of_divisor <<= 1
        if not sign:
            res = -res
        return min(max(res, -2**31), 2**31-1)
```