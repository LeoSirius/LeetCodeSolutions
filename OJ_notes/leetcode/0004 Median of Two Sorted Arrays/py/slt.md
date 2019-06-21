## 思路1 转化成求第K小的数

这道题有一定难度，这里先给出O(log(m+n))的解法。

首先我们要知道如何求一个排好序的数组的中位数。设数组总长度为l，如果数组a的长度是奇数，那么中位数就是`a[l/2]`，如果数组a的长度是偶数，那么中位数就是`(a[l/2] + a[l/2 - 1]) / 2`。

我们把问题中的两个数组看成是一个排好序的大数组，接下来就可以转化为求两个排序数组的第K大的数的问题。

我们先求出两个数组长度的一半`ia`和`ib`，如果是奇数，就像下取整（注意这里是长度，不要和大数组求中位数搞混）。如果`k > ia + ib`说明，k在a或b的后半段，至少不在a或b其中一个的前半段。我们找出较小的那个数组，把它的前半段抛弃。

同理，如果`k - 1 < ia + ib`，说明k在a或b的前半段，至少不在a或b其中一个的后半段。我们找出较大的那个数组，把它的后半段抛弃。

注意所有抛弃都包括了一半索引（`ia`和`ib`）所在的位置。如果抛弃的是前半段，则k也要减去抛弃的个数。注意抛弃的个数是`ia + 1`或`ib + 1`。比如a长度为6，`ia=3`，我们共抛弃了0123四个位置的数。有如a长度为7，`ia=3`，我们还是抛弃的四个数。


```py
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # 合并基数和偶数的情况，如果是基数，left == right 
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (self.findKth(nums1, nums2, left) + self.findKth(nums1, nums2, right)) / 2

    def findKth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k-1]
        if not nums2:
            return nums1[k-1]
        l1, l2 = len(nums1) // 2, len(nums2) // 2
        v1, v2 = nums1[l1], nums2[l2]

        # (l1 + l2) is base on index, but k is start from 1, so (k-1)
        if k - 1 > l1 + l2:
            # k 在总长度的后半段，抛弃前半段
            if v1 < v2:
                return self.findKth(nums1[l1+1:], nums2, k-(l1+1))
            else:
                return self.findKth(nums1, nums2[l2+1:], k-(l2+1))
        else:
            # discard second half
            if v1 < v2:
                return self.findKth(nums1, nums2[:l2], k)
            else:
                return self.findKth(nums1[:l1], nums2, k)
```