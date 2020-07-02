from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = dict()
        if t < 0: return False
        for i in range(len(nums)):
            nth = nums[i] // (t + 1)    # nth分别是(t+1)的0倍，1倍，2倍...
            if nth in bucket:           # 同一个桶内的数字最多相差t
                return True
            # 在相邻的桶中
            if nth - 1 in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return True
            if nth + 1 in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return True
            bucket[nth] = nums[i]
            # 这里相当于一个窗口，大小是k，超过则pop
            if i >= k: bucket.pop(nums[i - k] // (t + 1))
        return False


def test(test_name, nums, k, t, expected):
    res = Solution().containsNearbyAlmostDuplicate(nums, k, t)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,2,3,1]
    k1, t1 = 3, 0
    expected1 = True
    test("test1", nums1, k1, t1, expected1)

    nums2 = [1,0,1,1]
    k2, t2 = 1, 2
    expected2 = True
    test('test2', nums2, k2, t2, expected2)

    nums3 = [1,5,9,1,5,9]
    k3, t3 = 2, 3
    expected3 = False
    test('test3', nums3, k3, t3, expected3)


# Given an array of integers, find out whether there are two
# distinct indices i and j in the array such that the absolute
# difference between nums[i] and nums[j] is at most t and the
# absolute difference between i and j is at most k.
#
# Example 1:
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true

# Example 3:
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
