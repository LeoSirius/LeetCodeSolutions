### 思路1 利用hash的思想

由于最后要返回的是索引的数组。用hash的key来存放数组中一个元素的值，而用hash的value来存放那个值得索引。这样就建立了数组元素值对数组元素索引的映射。

find()的时间复杂是常量。

返回vector的顺序不重要。

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: nums' element, value: index of that element
        mapping = {}
        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if num_to_find in mapping.keys():
                return [i, mapping[num_to_find]]
            else:
                mapping[nums[i]] = i
```