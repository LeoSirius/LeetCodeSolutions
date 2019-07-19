class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        p = length - 1

        while p > 0 and nums[p-1] >= nums[p]:
            p -= 1

        reverse_len = length - p
        for i in range(reverse_len // 2):
            nums[p+i], nums[length-i-1] = nums[length-i-1], nums[p+i]

        if p > 0:
            for i in range(p, length):
                if nums[i] > nums[p-1]:
                    nums[p-1], nums[i] = nums[i], nums[p-1]
                    break