### 思路1 类似第26题，只是判断的对象是给定的一个val

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