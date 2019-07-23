class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def bi_search_left(nums, target):
            l, r = 0, len(nums)-1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1
        
        def bi_search_right(nums, target):
            l, r = 0, len(nums)-1
            while l < r:
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return r if nums[r] == target else -1
        
        return [bi_search_left(nums, target), bi_search_right(nums, target)]
