class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        res = sign * int(str(sign * x)[::-1])
        return 0 if res > 2 ** 31 -1 or res < -(2 ** 31) else res