class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        small_index = l
        l, r = 0, len(nums)-1
        if nums[small_index] <= target <= nums[r]:
            l = small_index
        else:
            r = small_index

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        return -1