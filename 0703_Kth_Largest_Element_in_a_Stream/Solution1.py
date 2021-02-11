from typing import *
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = nums
        self.k = k
        heapq.heapify(self.hp)

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        while len(self.hp) > self.k:
            heapq.heappop(self.hp)
        return self.hp[0]


def test1():
    obj = KthLargest(3, [4, 5, 8, 2])
    res1 = obj.add(3)
    res2 = obj.add(5)
    res3 = obj.add(10)
    res4 = obj.add(9)
    res5 = obj.add(4)

    if (res1, res2, res3, res4, res5) == (4,5,5,8,8):
        print('test1 success.')
    else:
        print('test1 failed.')


if __name__ == '__main__':
    test1()




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# Design a class to find the kth largest element in a stream. 
# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the 
# integer k and the stream of integers nums.
# int add(int val) Returns the element representing the kth largest 
# element in the stream.
#  

# Example 1:

# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]

# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // 4,5,8,2,3 return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
#  

# Constraints:

# 1 <= k <= 104
# 0 <= nums.length <= 104
# -104 <= nums[i] <= 104
# -104 <= val <= 104
# At most 104 calls will be made to add.
# It is guaranteed that there will be at least k elements in
#  the array when you search for the kth element.

