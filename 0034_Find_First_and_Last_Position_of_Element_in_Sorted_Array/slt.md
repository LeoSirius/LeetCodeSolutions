### 思路1 二分查找

首先我们说明一下二分查找，记住二分查找如果有重复的，找最左边和最右边的数的方法即可。

先来看看找左边的方法，不同于传统的二分查找，这里有两点不同：一是while的条件里没有等号，二是我们把下面的2和3归结为一个case：
1. If A[mid] < target, then the range must begins on the right of mid (hence i = mid+1 for the next iteration)
2. If A[mid] > target, it means the range must begins on the left of mid (j = mid-1)
3. If A[mid] = target, then the range must begins on the left of or at mid (j= mid)

2和3可以合并写成 2*. If A[mid] >= target, j = mid;

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def bisearch_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def bisearch_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return r if nums[r] == target else -1

        return [bisearch_left(nums, target), bisearch_right(nums, target)]
```