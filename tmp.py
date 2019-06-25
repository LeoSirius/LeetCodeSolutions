class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        sum = 0
        while sum < x:
            sum = sum*10 + x%10
            x //= 10
        
        return (x == sum) or (x == sum//10)

a = 0%10
print(a)