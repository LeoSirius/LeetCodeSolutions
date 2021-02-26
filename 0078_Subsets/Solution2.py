from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]  # init with empty subset

        for n in nums:
            # for every number in nums, add that number to every item in existed res
            # then add these new subs to res
            new_subs = [[n] + item for item in res]
            res += new_subs

        return res


def test(test_name, nums, expected):
    res = Solution().subsets(nums)
    res = [sorted(item) for item in res]
    expected = [sorted(item) for item in expected]
    res.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [1,2,3]
    expected1 = [
        [3],
        [1],
        [2],
        [1,2,3],
        [1,3],
        [2,3],
        [1,2],
        []
    ]
    test('test1', nums1, expected1)


