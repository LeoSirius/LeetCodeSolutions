### 思路1 二分查找

题目要求时间复杂度为O(logn)，必然用二分查找。但是不同于一般的二分查找，这个是绕pivot旋转过的。观察可以发现，如果nums[left] <= nums[mid],那么[left,mid] 一定为单调递增序列。反之[mid,right]则为有序单调自增序列。

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            
            if nums[low] <= nums[mid]:
                # 注意边界条件，如果target比nums[low]还小，说明是被pivot到了后面
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # 同样注意右边的边界条件，如果target比nums[right]还打，说明被pivot到了前面
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
```