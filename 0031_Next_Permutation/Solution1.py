from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                nums.reverse()
                return
            if nums[i] > nums[i-1]:
                max_idx = i
                break
        
        first_big_idx = len(nums) - 1    # first bigger than nums[max_idx-1] from right
        for i in range(len(nums) - 1, max_idx - 1, -1):
            if nums[max_idx-1] < nums[i]:
                first_big_idx = i
                break
        nums[max_idx-1], nums[first_big_idx] = nums[first_big_idx], nums[max_idx-1]
        tmp = nums[max_idx:]
        tmp.reverse()
        nums[max_idx:] = tmp


def test(test_name, nums, expected):
    slt = Solution()
    slt.nextPermutation(nums)
    if nums == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,2,3]
    expected1 = [1,3,2]
    test("test1", nums1, expected1)

    nums2 = [3,2,1]
    expected2 = [1,2,3]
    test("test2", nums2, expected2)

    nums3 = [1,1,5]
    expected3 = [1,5,1]
    test("test3", nums3, expected3)

    nums4 = [1,3,2]
    expected4 = [2,1,3]
    test("test4", nums4, expected4)
