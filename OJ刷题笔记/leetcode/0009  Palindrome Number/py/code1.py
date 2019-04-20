class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        ranger = 1
        while x // ranger >= 10:
            ranger *= 10
            
        while x:
            left = x // ranger
            right = x % 10
            if left != right:
                return False
            
            x = (x % ranger) // 10
            ranger //= 100
        
        return True