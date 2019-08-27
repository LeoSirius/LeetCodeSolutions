## 思路1 利用递归化解为2sum

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

## 思路2 思路同3sum，只是多了一重循环

这个思路关键是处理好重复的跳过。由于我们是从左边往右边遍历的，所以需要往左移的case直接pass掉。

```cpp
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        if (nums.size() < 4) return res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 3; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int three_target = target - nums[i];

            for (int j = i + 1; j < nums.size() - 2; j++) {
                if (j > i+1 && nums[j] == nums[j-1]) continue;
                int two_target = three_target - nums[j];
                int l, r;
                l = j + 1; r = nums.size() - 1;
                while (l < r) {
                    int left, right;
                    left = nums[l];;
                    right = nums[r];
                    if (left + right == two_target) {
                        res.push_back(vector<int> {nums[i], nums[j], left, right});
                        while (l < r && nums[l] == left) l++;
                        while (l < r && nums[r] == right) r--; 
                    } else if (left + right < two_target) l++;
                    else r--;
                }
            }
        }
        return res;
    }
};
```