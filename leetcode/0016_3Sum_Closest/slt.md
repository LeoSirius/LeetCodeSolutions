## 思路1 类似3sum的思路1

不过有两点不同。一是只用返回一个确切的数。二是题目明确告诉只有一个答案，所以重复判断也不需要了。

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(target - s) < abs(target - closest):
                    closest = s

                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
        return closest
```