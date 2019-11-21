### 思路1 DFS

和上一道题非常类似。两个不同之处：一是对重复元素的检查，二是一个元素只用一次

上一题candidates里面没有重复的元素，所以所有的组合必然是不同的。这题里面candidates里面有重复的元素，为了保证没有重复的组合，需要检查

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return # backtracking
        if not target:
            res.append(path)
            return
        for i in range(index, len(nums)):
            # skip duplicate
            if i > index and nums[i] == nums[i-1]:
                continue
            # index + 1, because one element could only be used once
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)
```