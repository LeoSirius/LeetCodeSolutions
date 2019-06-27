## 思路1 转化为TwoSum

首先用sort给数组排序。然后我们用i依次遍历每个元素。先确定了i最外层的最外层的一个数，那么在i的依次循环内，问题就转化为TwoSum了，再用l和r分别指向i的下一个元素和最后一个元素。最后就是把这3个元素的和与0进行比较了。如果比0小，则把l向右移动一位。反之则把r向左移动一位。

注意题目要求是unique triplets，所以有重复的还得跳过。ilr三个指针都有是否重复的判断。

```cppclass Solution {
public:
    vector<vector<int> > threeSum(vector<int>& nums) {
        vector<vector<int> > res;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); ++i){
            int target = -nums[i];
            int left = i+1;
            int right = nums.size()-1;

            while(left < right){
                if(nums[left]+nums[right] > target){
                    --right;
                }else if(nums[left]+nums[right] < target){
                    ++left;
                }else{
                    vector<int> triple(3,0);
                    triple[0] = nums[i];
                    triple[1] = nums[left];
                    triple[2] = nums[right];
                    res.push_back(triple);

                    while(left < right && nums[left] == triple[1]) ++left;
                    while(left < right && nums[right] == triple[2]) --right;
                }
            }
            while(i+1 < nums.size() && nums[i+1] == nums[i]) ++i;
        }
        return res;
    }
};
```

```python
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # notice the difference with cpp code, l and r must be at 
                    # the non-duplicate char's index
                    l += 1; r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return res
```