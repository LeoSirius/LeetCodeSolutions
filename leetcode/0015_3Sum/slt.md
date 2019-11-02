## 思路1 思路同TwoSum，排序后遍历所有组合

首先用sort给数组排序。然后我们用i依次遍历每个元素。先确定了i最外层的最外层的一个数，那么在i的依次循环内，问题就转化为TwoSum了，再用l和r分别指向i的下一个元素和最后一个元素。最后就是把这3个元素的和与0进行比较了。如果比0小，则把l向右移动一位。反之则把r向左移动一位。

注意题目要求是unique triplets，所以有重复的还得跳过。ilr三个指针都有是否重复的判断。

```cppclass Solution {
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int l, r;
            l = i + 1; r = nums.size() - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    int left = nums[l];
                    int right = nums[r];
                    res.push_back(vector<int> {nums[i], left, right});
                    while (l < r && left == nums[l]) l++;
                    while (l < r && right == nums[r]) r--;
                } else if (sum > 0) {
                    r--;
                } else {
                    l++;
                }
            }
        }
        return res;
    }
};
```

注意跳过重复的代码和cpp中不一样的地方

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                left, right = nums[l], nums[r]
                three_sum = nums[i] + left + right
                if three_sum == 0:
                    res.append([nums[i], left, right])
                    while l < r and nums[l] == left:
                        l += 1
                    while l < r and nums[r] == right:
                        r -= 1
                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1
        return res
```