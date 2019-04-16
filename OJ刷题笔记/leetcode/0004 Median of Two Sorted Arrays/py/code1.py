class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.Kth(nums1, nums2, l // 2)
        else:
            return (self.Kth(nums1, nums2, l // 2) + self.Kth(nums1, nums2, l // 2 - 1)) / 2
        
    def Kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        va, vb = a[ia], b[ib]
        
        if k > ia + ib:
            if va > vb:
                return self.Kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.Kth(a[ia + 1:], b, k - ia - 1)
        else:
            if va < vb:
                return self.Kth(a, b[:ib], k)
            else:
                return self.Kth(a[:ia], b, k)
        
