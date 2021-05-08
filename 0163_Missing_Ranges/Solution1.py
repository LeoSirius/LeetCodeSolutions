from typing import *

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res_pairs = [(lower, upper)]

        for n in nums:
            new_res = []
            for pair in res_pairs:
                if pair[0] <= n <= pair[1]:
                    new_res.append((pair[0], n-1))
                    new_res.append((n+1, pair[1]))
                    break
                new_res.append(pair)
            res_pairs = new_res

        res_strs = []
        for pair in res_pairs:
            if pair[0] > pair[1]:
                continue
            elif pair[0] == pair[1]:
                res_strs.append(str(pair[0]))
            else:
                res_strs.append(str(pair[0]) + '->' + str(pair[1]))

        return res_strs



def test(test_name, nums, lower, upper, expected):
    res = Solution().findMissingRanges(nums, lower, upper)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == '__main__':
    nums1 = [0,1,3,50,75]
    lower1 = 0
    upper1 = 99
    expected1 = ["2","4->49","51->74","76->99"]
    test('test1', nums1, lower1, upper1, expected1)

    nums2 = []
    lower2 = 1
    upper2 = 1
    expected2 = ["1"]
    test('test2', nums2, lower2, upper2, expected2)

    nums3 = []
    lower3 = -3
    upper3 = -1
    expected3 = ["-3->-1"]
    test('test3', nums3, lower3, upper3, expected3)

    nums4 = [-1]
    lower4 = -1
    upper4 = -1
    expected4 = []
    test('test4', nums4, lower4, upper4, expected4)

    nums5 = [-1]
    lower5 = -2
    upper5 = -1
    expected5 = ["-2"]
    test('test5', nums5, lower5, upper5, expected5)
