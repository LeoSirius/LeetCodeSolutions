### 思路1 类似第26题，只是判断的对象是给定的一个val

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left_most = 0;
        int len_nums = nums.size();
        if (len_nums == 0){
            return 0;
        }
        for(int i = 0; i < len_nums; i++){
            if(nums[i] != val){
                nums[left_most++] = nums[i];
            }
        }
        return left_most;
    }
};
```

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        new_tail = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[new_tail] = nums[i]
                new_tail += 1
        return new_tail
```