### 思路1 使用python的列表表达式

如果target在nums中，比如`[10,20,30,40,50], target = 30`，列表表达式结果是`[10,20]`长度是2，就是30的index。

如果target不再nums中，比如`[10,20,30,40,50], target = 31`，列表表达式的结果是`[10,20,30]`长度是3，正好是31要插入的index

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([x for x in nums if x < target])
```