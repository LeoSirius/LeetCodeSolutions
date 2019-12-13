### 思路1 二分查找

首先我们说明一下二分查找，记住二分查找如果有重复的，找最左边和最右边的数的方法即可。


先找左边界，再找右边界。找左边界从右边逼近，找右边界从左边逼近找左边界的方法：

1. target < A[mid]，左边界索引一定小于mid，right = mid - 1
2. target = A[mid]，左边界就是mid或小于mid，right = mid
3. target > A[mid]，左边界大于mid，left = mid + 1

很多解答都把1和2写在了一起，即（综合1和2，当`target <= A[mid]`时，right = mid;）其实这样不好理解，

注意找右边的时候mid要加1，因为默认是向左对齐的。



2和3可以合并写成 2*. If A[mid] >= target, j = mid;

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def bisearch_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def bisearch_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return r if nums[r] == target else -1

        return [bisearch_left(nums, target), bisearch_right(nums, target)]
```



利用二分思想先找其左边界，再找其右边界即可，注意找左边界的时候，由右侧逼近；找右边界的时候，由左侧逼近，即可。

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res(2,-1);
        if(nums.empty()) return res;
        int n=nums.size(),l=0,r=n-1;
        while(l<r){
            int m=l+(r-l)/2;
            if(nums[m]>=target) r=m;
            else l=m+1;
        }
        if(nums[l]!=target) return res;
        res[0]=l;
        r=n;
        while(l<r){
            int m=l+(r-l)/2;
            if(nums[m]<=target) l=m+1;
            else r=m;
        }
        res[1]=l-1;
        return res;
    }
};