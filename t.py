from typing import *


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == res:
                cnt += 1
            else:
                cnt -= 1
            print(f'cnt = {cnt}')
            if cnt == 0:
                print(' in in')
                res = nums[i]
                cnt = 1
            # print(f'nums[i] = {nums[i]}, cnt = {cnt}')
        print(f'res = {res}')
        print(f'nums.count(res) = {nums.count(res)}')
        return res if nums.count(res) >= len(nums)//2 else -1


def test(test_name, nums, expected):
    res = Solution().majorityElement(nums)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    nums1 = [1,2,5,9,5,9,5,5,5]
    expected1 = 5
    # test('test1', nums1, expected1)

    # nums2 = [3,2]
    # exepcted2 = -1
    # test('test2', nums2, exepcted2)

    # nums3 = [2,2,1,1,1,2,2]
    # expected3 = 2
    # test('test3', nums3, expected3)

    nums4 = [8,8,7,7,7]
    expected4 = 7
    test('test4', nums4, expected4)
