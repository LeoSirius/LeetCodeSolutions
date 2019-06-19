## 思路1 利用一个buff_dict

设`a + b = target`利用一个字典，key存放a或b其中一个，value则是key在原数组中的索引。依次遍历数组，当第一次遇到a或b时，把他们放入`dict`，第二次遇到a或b时，直接返回即可。

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