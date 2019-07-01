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

## 思路2 利用迭代化解为2sum，类似于3sum的思路

这个思路关键是处理好重复的跳过。由于我们是从左边往右边遍历的，所以需要往左移的case直接pass掉。

```cpp
// 目前这个答案leetcode会报AddressSanitizer: heap-buffer-overflow
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> total;
        int n = nums.size();
        if(n < 4) return total;
        sort(nums.begin(), nums.end());
        
        for(int i = 0; i < n - 3; ++i){
            if(i > 0 && nums[i-1] == nums[i]) continue;
            if(nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target) break;   // 最小的四个都大于target
            if(nums[i]+nums[n-1]+nums[n-2]+nums[n-3] < target) continue; // 加上最大的三个都还小于target，说明i要右移
            for(int j = i + 1; j < n - 2; ++j){
                if(j > i+1 && nums[j-1] == nums[j]) ++j;
                if(nums[i]+nums[j]+nums[j+1]+nums[j+2] > target) break;
                if(nums[i]+nums[j]+nums[n-1]+nums[n-2] < target) continue;
                int l = j+1;
                int r = n-1;
                while(l < r){
                    int sum = nums[i] + nums[j] + nums[l] + nums[r];
                    if(sum == target){
                        total.push_back(vector<int>{nums[i], nums[j], nums[l], nums[r]});
                        while(l < r && nums[l] == nums[l+1]) ++l;
                        while(l < r && nums[r] == nums[r-1]) --r;
                        ++l, --r;
                    }else if(sum > target){
                        --r;
                    }else{
                        ++l;
                    }
                }
            }
        }
        return total;
    }
};
```