class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        reversed_num = sign * int((str(sign*x))[::-1])
        if reversed_num > 2**31-1 or reversed_num < -2**31:
            return 0
        else:
            return reversed_num