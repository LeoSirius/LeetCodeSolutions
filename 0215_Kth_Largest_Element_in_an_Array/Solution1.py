from typing import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def _partition(l, r):
            pivot = nums[l]
            j = l
            for i in range(l+1, r+1):
                if nums[i] < pivot:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[j] = nums[j], nums[l]
            return j

        size = len(nums)
        target_index = size - k
        l, r = 0, size-1

        while True:
            idx = _partition(l, r)
            if idx == target_index:
                return nums[idx]
            elif idx < target_index:
                l = idx + 1
            else:
                r = idx - 1


def test(test_name, nums, k, expected):
    res = Solution().findKthLargest(nums, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [3,2,1,5,6,4]
    k1 = 2
    expected1 = 5
    test('test1', nums1, k1, expected1)

    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    expected2 = 4
    test('test2', nums2, k2, expected2)

# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.

# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
