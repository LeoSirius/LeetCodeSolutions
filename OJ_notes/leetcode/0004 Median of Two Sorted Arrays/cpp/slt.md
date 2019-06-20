## 思路1 转化为求Kth smallest的数

我们可以将基数情况和偶数情况合并，如果是基数，就求两次同样的。

unsolved code 

```cpp
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    double Kth(vector<int>& nums1, int start1, int end1, vector<int>& nums2, int start2, int end2, int k){
        int l1 = end1 - start1 + 1;
        int l2 = end1 - start1 + 1;
        // make sure nums1 is shorter or equal than nums2
        if(l1 > l2) return Kth(nums1, start1, end1, nums2, start2, end2, k);
        if(l1 == 0) return nums2[start2 + k - 1]; // k is not index, so minus 1
        //cout << "k = " << k << endl;
        if(k == 1){
            cout << "in if k == 1" << endl;
            return min(nums1[start1], nums2[start2]);
        }

        // 我们把当前截取后的两个数组的第k/2个数进行比较，然后抛去nums1或nums2的前半部分
        // mid1, mid2 是索引
        // A [ 1 ]，A [ 2 ]，A [ 3 ]，A [ k / 2] … ，B[ 1 ]，B [ 2 ]，B [ 3 ]，B[ k / 2] … ，
        //如果 A [ k / 2 ] < B [ k / 2 ] ，那么 A [ 1 ]，A [ 2 ]，A [ 3 ]，A [ k / 2] 都不可能是第 k 小的数字。
        int mid1 = start1 + min(l1, k/2) - 1;
        int mid2 = start2 + min(l2, k/2) - 1;
        cout << "===begin===" << endl;
        cout << "nums2[mid2] = " << nums2[mid2] << endl;
        cout << "nums1[mid1] = " << nums1[mid1] << endl;
        cout << "k = " << k << endl;
        cout << "===end===" << endl;
        if(nums2[mid2] < nums1[mid1]){
            cout << "k-(mid2-start2+1) = " << k-(mid2-start2+1) << endl;
            return Kth(nums1, start1, end1, nums2, mid2+1, end2, k-(mid2-start2+1));
        }else{
            cout << "k-(mid1-start1+1) = " << k-(mid1-start1+1) << endl;
            return Kth(nums1, mid1+1, end1, nums2, start2, end2, k-(mid1-start1+1));
        }
    }
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // 将基数和偶数情况合并，如果是基数，left=right，就求两次同样的
        int l1 = nums1.size();
        int l2 = nums2.size();
        // 下面两种特殊情况是索引，从0开始，所以往左边减
        if(l1 == 0){
            return (nums2[(l2)/2] + nums2[(l2-1)/2]) / 2;
        }
        if(l2 == 0){
            return (nums1[(l1)/2] + nums1[(l1-1)/2]) / 2;
        }
        int left = (l1 + l2 + 1) / 2;   // left 是划分的左边，注意这里是k，是从1开始的
        int right = (l1 + l2 + 2) / 2;  // right 是划分的右边
        cout << "left = " << left << "  right = " << right << endl;
        return (Kth(nums1, 0, l1 - 1, nums2, 0, l2 - 1, left) + 
                Kth(nums1, 0, l1 - 1, nums2, 0, l2 - 1, right)) / 2.0;
    }
};

int main(){
    Solution * s = new Solution();
    int v1[1] = {100000};
    int v2[1] = {100001};
    vector<int> vec1(v1, v1+1);
    vector<int> vec2(v2, v2+1);

    cout << s->findMedianSortedArrays(vec1, vec2) << endl;

    return 0;
}
```