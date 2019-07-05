### 思路1 就地算法

注意，这道题的返回结果使用引用传出去。

我们用new_tail来作为已经整理好的没有重复元素的数组的最后一个索引。然后用i去找后面的元素，如果重复就跳过，如果i和new_tail的元素不同，则把i上的元素放到new_tail后面。时间复杂度为O(n),空间复杂度为O(1)。

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new_tail = 0
        for i in range(1, len(nums)):
            if nums[new_tail] != nums[i]:
                new_tail += 1
                nums[new_tail] = nums[i]

        return new_tail+1
```