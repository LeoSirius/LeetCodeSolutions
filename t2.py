from typing import *


class Trie:
    def __init__(self):
        self.bits = [None] * 2

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        HIGH_BIT = 30

        def add(n):
            node = root
            for k in range(HIGH_BIT, -1, -1):
                bit = (n >> k) & 1
                if not node.bits[bit]:
                    node.bits[bit] = Trie()
                node = node.bits[bit]
        
        def check(n):
            




def test(test_name, nums, expected):
    res = Solution().findMaximumXOR(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [3,10,5,25,2,8]
    expected1 = 28
    test('test1', nums1, expected1)

    nums2 = [0]
    expected2 = 0
    test('test2', nums2, expected2)

    nums3 = [2,4]
    expected3 = 6
    test('test3', nums3, expected3)

    nums4 = [8,10,2]
    expected4 = 10
    test('test4', nums4, expected4)

    nums5 = [14,70,53,83,49,91,36,80,92,51,66,70]
    expected5 = 127
    test('test5', nums5, expected5)

    nums6 = [4,6,7]
    expected6 = 3
    test('test6', nums6, expected6)
