class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rever_num = 0
        while rever_num < x:
            rever_num = rever_num * 10 + x % 10
            x //= 10
        return rever_num == x or rever_num // 10 == x