### 思路1 二分查找

首先我们说明一下二分查找，记住二分查找如果有重复的，找最左边和最右边的数的方法即可。


```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(A, target):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if target > A[mid]: 
                    left = mid + 1
                else: 
                    right = mid - 1
            return left

        def binarySearchRight(A, target):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2

                if target < A[mid]: 
                    right = mid - 1
                else: 
                    left = mid + 1
            return right
            
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return [left, right] if left <= right else [-1, -1]
```