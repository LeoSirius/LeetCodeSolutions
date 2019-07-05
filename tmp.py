class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new_tail = 0
        for i in range(1, len(nums)):
            if nums[new_tail] != nums[i]:
                new_tail += 1
                nums[new_tail] = nums[i]

        return new_tail+1