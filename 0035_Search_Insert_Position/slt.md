### 思路1 二分查找

如果target不在数组中的话，最后跳出循环时，low = high + 1，这时的low就是应该插入的位置。事件复杂度O(logn)

### 思路2 直接顺序查找

时间复杂度O(n)。这道题跑出来的实际时间，线性复杂度用的时间比对数复杂度还少得多。

```cpp
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size(); ++i){
            if(nums[i] >= target){
                return i;
            }
        }
        return nums.size();
    }
};
```

python中可以使用列表表达式

如果target在nums中，比如`[10,20,30,40,50], target = 30`，列表表达式结果是`[10,20]`长度是2，就是30的index。

如果target不再nums中，比如`[10,20,30,40,50], target = 31`，列表表达式的结果是`[10,20,30]`长度是3，正好是31要插入的index

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([x for x in nums if x < target])
```
