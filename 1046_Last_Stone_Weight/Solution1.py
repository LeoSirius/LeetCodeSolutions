from typing import *
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_hp = []
        heapq.heapify(max_hp)
        for n in stones:
            heapq.heappush(max_hp, -n)
        
        while len(max_hp) >= 2:
            print
            m1, m2 = -heapq.heappop(max_hp), -heapq.heappop(max_hp)
            if m1 > m2:
                heapq.heappush(max_hp, -(m1-m2))
        
        return -max_hp[0] if max_hp else 0


def test(test_name, stones, expected):
    res = Solution().lastStoneWeight(stones)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    stones1 = [2,7,4,1,8,1]
    expected1 = 1
    test('test1', stones1, expected1)

    stones2 = [2,2]
    expected2 = 0
    test('test2', stones2, expected2)


# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together. 
#  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of 
# weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone 
# (or 0 if there are no stones left.)


# Example 1:

# Input: [2,7,4,1,8,1]
# Output: 1

# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that'
# s the value of last stone.
#  

# Note:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
