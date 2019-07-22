### 思路1 二分查找，先找最小元素

时间有限制O(log n)。显然我们必须使用二分查找，但是又不能直接用二分查找。先找到最小元素的index，再判断target是在最小元素的前面还是后面，再用常规的二分查找。

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int len = nums.size();
        if(len == 0) return -1;

        int l, r, m;
        l = 0, r = len - 1;

        // find smallest's index
        // 循环结束时l = r， m可能等于l，也可能比l小1
        while(l < r){
            m = (l+r) / 2;
            if(nums[m] > nums[r]) l = m+1;
            else r = m;
        }

        // 以最小索引为界，放弃target不可能存在的那一半
        int s = l;
        l = 0, r = len - 1;
        if(nums[s] <= target && target <= nums[r])l = s;
        else r = s;

        while(l <= r){
            m = (l + r) / 2;
            if(nums[m] == target) return m;
            else if(nums[m] > target) r = m - 1;
            else l = m + 1;
        }
        return -1;
    }
};
```

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        small_index = l
        l, r = 0, len(nums)-1
        if nums[small_index] <= target <= nums[r]:
            l = small_index
        else:
            r = small_index
        
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
```