class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (self.findKth(nums1, nums1, left) + self.findKth(nums1, nums2, right)) / 2


    def findKth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k-1]
        if not nums2:
            return nums1[k-1]
        
        l1, l2 = len(nums1) // 2, len(nums2) // 2
        v1, v2 = nums1[l1], nums2[l2]

        if k-1 > l1+ l2:
            if v1 < v2:
                return self.findKth(nums1[l1+1:], nums2, k-(l1+1))
            else:
                return self.findKth(nums1, nums2[l2+1:], k-(l2+1))
        else:
            if v1 < v2:
                return self.findKth(nums1, nums2[:l2], k)
            else:
                return self.findKth(nums1[:l1], nums2, k)
