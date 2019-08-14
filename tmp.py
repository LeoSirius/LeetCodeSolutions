class Solution:
    def find_Kth(self, nums1, nums2, k):
        if not nums1: return nums2[k-1]
        if not nums2: return nums1[k-1]

        l1, l2 = len(nums1) // 2, len(nums2) // 2
        v1, v2 = nums1[l1], nums2[l2]

        if (k-1) > (l1+l2):
            if v1 < v2:
                return self.find_Kth(nums1[l1+1:], nums2, k-(l1+1))
            else:
                return self.find_Kth(nums1, nums2[l2+1:], k-(l2+1))
        else:
            if v1 < v2:
                return self.find_Kth(nums1, nums2[:l2], k)
            else:
                return self.find_Kth(nums1[:l1], nums2, k)


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        left, right = (len1+len2+1) // 2, (len1+len2+2) // 2
        return (self.find_Kth(nums1, nums2, left) + self.find_Kth(nums1, nums2, right)) / 2