## 思路1 排序后遍历所有组合

> Time complexity: O(n^2)

注意题目要求是unique triplets，所以有重复的还得跳过。ilr三个指针都有是否重复的判断。

如果用下面的方法，其实也是O(n^2)。因为twoSum本身是O(n)。这里排序后遍历也是O(n^2)，因为是排过序的。

```
for a in nums:
    target = 2
    twoSum(target)
```

