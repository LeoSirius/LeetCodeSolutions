from typing import *


class Trie:
    def __init__(self):
        self.bits = [None] * 2   # bits[0] 表示 0，bits[1] 表示 1

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        HIGH_BIT = 30    # 最高位的索引，一共 31 位

        # 把 n 插入前缀树中
        def add(n: int):
            node = root
            for k in range(HIGH_BIT, -1, -1):
                bit = (n >> k) & 1
                if not node.bits[bit]:
                    node.bits[bit] = Trie()
                node = node.bits[bit]

        # n 是 nums[i]
        # 这个函数找出所有 [nums[0], nums[i-1]] 与 nums[i] 异或的最大值
        def check(n: int) -> int:
            node = root
            x = 0
            for k in range(HIGH_BIT, -1, -1):
                bit = (n >> k) & 1
                if bit == 0:
                    # nums[i] 的第 k 个二进制位为 0，应当往表示 1 的子节点走
                    if node.bits[1]:
                        node = node.bits[1]
                        x = x * 2 + 1
                    else:
                        node = node.bits[0]
                        x *= 2
                else:
                    # nums[i] 的第 k 个二进制位为 0，应当往表示 0 的子节点走
                    if node.bits[0]:
                        node = node.bits[0]
                        x = x * 2 + 1
                    else:
                        node = node.bits[1]
                        x *= 2
            return x

        x = 0
        for i in range(1, len(nums)):
            add(nums[i-1])
            x = max(x, check(nums[i]))

        return x


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
