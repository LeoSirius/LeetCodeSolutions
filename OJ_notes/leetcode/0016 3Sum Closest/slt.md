## 思路1 类似3sum的思路1

不过有两点不同。一是只用返回一个确切的数。二是题目明确告诉只有一个答案，所以重复判断也不需要了。

```cpp
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int closest = nums[0]+nums[1]+nums[2];
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size()-2; i++){
            int left = i + 1;
            int right = nums.size()-1;
            while(left < right){
                int sum = nums[i]+nums[left]+nums[right];
                if(sum == target){
                    return sum;
                }
                if(abs(target-sum) < abs(target-closest)){
                    closest = sum;
                }
                if(sum > target){
                    --right;
                }else{
                    ++left;
                }
            }
        }
        return closest;
    }
};
```

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(target - s) < abs(target - result):
                    result = s

                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
        return result
```