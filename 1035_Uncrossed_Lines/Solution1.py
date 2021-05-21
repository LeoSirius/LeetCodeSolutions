from typing import *

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        _len1, _len2 = len(nums1), len(nums2)
        dp = [[0] * (_len2+1) for _ in range(_len1+1)]

        for i in range(_len1):
            for j in range(_len2):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[-1][-1]


def test(test_name, nums1, nums2, expected):
    res = Solution().maxUncrossedLines(nums1, nums2)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums11 = [1,4,2]
    nums21 = [1,2,4]
    expected1 = 2
    test('test1', nums11, nums21, expected1)

    nums12 = [2,5,1,2,5]
    nums22 = [10,5,2,1,5,2]
    expected2 = 3
    test('test2', nums12, nums22, expected2)

    nums13 = [1,3,7,1,7,5]
    nums23 = [1,9,2,5,1]
    expected3 = 2
    test('test3', nums13, nums23, expected3)
