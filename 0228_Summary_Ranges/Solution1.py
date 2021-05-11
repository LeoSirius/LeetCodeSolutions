from typing import *

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        pairs = []
        last_l = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                continue
            pairs.append((last_l, nums[i-1]))
            last_l = nums[i]
        pairs.append((last_l, nums[-1]))

        res = []
        for pair in pairs:
            if pair[0] == pair[1]:
                res.append(str(pair[0]))
            else:
                res.append(f'{str(pair[0])}->{str(pair[1])}')
        return res


def test(test_name, nums, expected):
    res = Solution().summaryRanges(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [0,1,2,4,5,7]
    expected1 = ["0->2","4->5","7"]
    test('test1', nums1, expected1)

    nums2 = [0,2,3,4,6,8,9]
    expected2 = ["0","2->4","6","8->9"]
    test('test2', nums2, expected2)

    nums3 = []
    expected3 = []
    test('test3', nums3, expected3)

    nums4 = [-1]
    expected4 = ["-1"]
    test('test4', nums4, expected4)

    nums5 = [0]
    expected5 = ["0"]
    test('test5', nums5, expected5)
