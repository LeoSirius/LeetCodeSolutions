## 思路1 转化为求Kth smallest的数

我们可以将长度基数情况和偶数情况合并，如果是基数，就求两次同样的。

先判断k-1是在总索引的前半部分还是后半部分。如果k在后半部分，则我们抛弃两个数组中位数较小的那个数组的前半部分，否则抛弃两个数组中位数较大的那个数组的后半部分。

```cpp
class Solution {
    double findKth(vector<int>& nums1, vector<int>& nums2, int k){
        if(!nums1.size()) return nums2[k-1];
        if(!nums2.size()) return nums1[k-1];

        // 这里是中间元素的索引，如果有5个元素，则l = 2
        // 如果有6个元素，则l = 3
        int l1, l2, v1, v2;
        l1 = nums1.size() / 2;
        l2 = nums2.size() / 2;
        v1 = nums1[l1]; v2 = nums2[l2];

        if((k-1) > l1+l2){
            if(v1 < v2){
                // 区间复制构造函数是左闭右开的
                // nums1.begin()+l1+1 保证把l1所在的位置也抛弃了
                vector<int> nums1_second(nums1.begin()+l1+1, nums1.end());
                return findKth(nums1_second, nums2, k-(l1+1));
            }else{
                vector<int> nums2_second(nums2.begin()+l2+1, nums2.end());
                return findKth(nums1, nums2_second, k-(l2+1));
            }
        }else{
            if(v1 < v2){
                // 区间复制构造函数是左闭右开的
                // nums2.begin()+l2 保证把l2所在的位置也抛弃了
                vector<int> nums2_first(nums2.begin(), nums2.begin()+l2);
                return findKth(nums1, nums2_first, k);
            }else{
                vector<int> nums1_first(nums1.begin(), nums1.begin()+l1);
                return findKth(nums1_first, nums2, k);
            }
        }
    }
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // 如果是基数，如5，则left = right = 3
        // 如果是偶数，如6，则left = 3, right = 4
        int left = (nums1.size() + nums2.size() + 1) / 2;
        int right = (nums1.size() + nums2.size() + 2) / 2;
        return (findKth(nums1, nums2, left) + findKth(nums1, nums2, right)) / 2;
    }
};
```

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
            return nums2[k-1] # k是从1开始算的，所以这里减1
        if not nums2:
            return nums1[k-1]
        # 下面是两个中间位置的值，基数长度则就是正中间，偶数则靠右1位
        l1, l2 = len(nums1) // 2, len(nums2) // 2
        v1, v2 = nums1[l1], nums2[l2]

        # (l1 + l2) is base on index, but k is start from 1, so (k-1)
        if k - 1 > l1 + l2:
            # k 在总长度的后半段，抛弃前半段，被抛弃的元素个数是l1+1或l2+1，用k减去它们
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