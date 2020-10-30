from typing import *

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = [[i, j] for i in nums1 for j in nums2]
        pairs.sort(key=lambda i:i[0]+i[1])
        return pairs[:k]


def test(test_name, nums1, nums2, k, expected):
    res = Solution().kSmallestPairs(nums1, nums2, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    nums11 = [1,7,11]
    nums21 = [2,4,6]
    k1 = 3
    expected1 = [[1,2],[1,4],[1,6]]
    test('test1', nums11, nums21, k1, expected1)

    nums12 = [1,1,2]
    nums22 = [1,2,3]
    k2 = 2
    expected2 = [[1,1],[1,1]]
    test('test2', nums12, nums22, k2, expected2)

    nums13 = [1,2]
    nums23 = [3]
    k3 = 3
    expected3 = [[1,3],[2,3]]
    test('test3', nums13, nums23, k3, expected3)


# You are given two integer arrays nums1 and nums2 sorted in ascending order
#  and an integer k.

# Define a pair (u,v) which consists of one element from the first array and 
# one element from the second array.

# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

# Example 1:

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]] 
# Explanation: The first 3 pairs are returned from the sequence: 
#              [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

# Example 2:

# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence: 
#              [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

# Example 3:

# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

