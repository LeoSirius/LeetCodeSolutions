class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                left, right = nums[l], nums[r]
                sum = nums[i] + left + right
                if sum == 0:
                    res.append([nums[i], left, right])
                    while l < r and nums[l] == left:
                        l+=1
                    while l < r and nums[r] == right:
                        r-=1
                elif sum > 0:
                    r-=1
                else:
                    l += 1
        return res

