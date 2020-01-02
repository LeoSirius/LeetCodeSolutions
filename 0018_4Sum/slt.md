## 思路1 思路同3sum，只是多了一重循环

我们查重检查的是同一个索引指向的下一个元素和当前元素是否相同。而不是i和j和l和r所指的元素是否相同

vector<int> nums2 = {-3,-2,-1,0,0,1,2,3};
int target2 = 0;
vector<vector<int>> expected2 = {
    {-3,-2,2,3},
    {-3,-1,1,3},
    {-3,0,0,3},
    {-3,0,1,2},
    {-2,-1,0,3},
    {-2,-1,1,2},
    {-2,0,0,2},   这里有两个0是因为j和l都是0。
    {-1,0,0,1}
};


## 思路2 利用递归化解为2sum

注意我们是排好序的，所以在一开始可以直接把一些情况pass掉

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def Nsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or nums[0]*N > target or nums[-1]*N < target:
                return
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        # because there is only left++, right did not move,
                        # so we only check duplicate from left
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        Nsum(nums[i+1:], target - nums[i], N-1, result+[nums[i]], results)

        results = []
        Nsum(sorted(nums), target, 4, [], results)
        return results
```

