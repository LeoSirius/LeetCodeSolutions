class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        closes_sum = nums[0] + nums[1] + nums[2]
        min_diff = abs(target - closes_sum)
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            s = nums[i] + nums[l] + nums[r]
            while l < r:
                if s == target:
                    return s
                elif s > target:
                    r -= 1
                else:
                    l += 1
                s = nums[i] + nums[l] + nums[r]
                if min_diff > abs(target - s):
                    min_diff = abs(target - s)
                    closes_sum = s
        return closes_sum

s = Solution()
res = s.threeSumClosest([0,2,1,-3], 1)
print(res)