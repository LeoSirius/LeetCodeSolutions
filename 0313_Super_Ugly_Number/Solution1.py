from typing import *

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1 for _ in range(n)]
        p_dict = {k:0 for k in primes}  # k is primes, v is pointer

        for i in range(1, n):
            dp[i] = min([dp[p_dict[prime]]*prime for prime in p_dict])
            for prime, p in p_dict.items():
                if dp[i] == dp[p] * prime:
                    p_dict[prime] += 1
        return dp[-1]

def test(test_name, n, primes, expected):
    res = Solution().nthSuperUglyNumber(n, primes)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 12
    primes1 = [2,7,13,19]
    expected1 = 32
    test('test1', n1, primes1, expected1)


# Write a program to find the nth super ugly number.

# Super ugly numbers are positive numbers whose all prime factors are 
# in the given prime list primes of size k.

# Example:

# Input: n = 12, primes = [2,7,13,19]
# Output: 32 
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
#              super ugly numbers given primes = [2,7,13,19] of size 4.

# Note:

# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

