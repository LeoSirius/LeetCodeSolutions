### 思路1

首先我们搞清楚什么是next permutation。1、2、3的全排列：

```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

可见next permutation就是全排列顺序中的下一个。

再来看一个长一点的例子。有如下的一个数组

```
1　　2　　7　　4　　3　　1
```

下一个排列为：

```
1　　3　　1　　2　　4　　7
```

观察可以发现，再给出的数组中，2之后的数字都是降序排列的，我们把2后面第一个比2大的数字（这里是3）和2交换，然后让3后面的数字升序排列。

简单思路的证明：从7开始是降序的，也就是说7 4 3 1不可能通过重新排列构成更大的数字。如果要得到next permutation，那么必须把2这个位置的数字给换掉才行，而且只能换成比2大的数字在才能使next permutation > current permutation.至于换成多大的数字，很明显的需要换成在2后面的数字中刚好比2大的数字。

```cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size(), k, l;
        for(k = n - 2; k >= 0; --k){
            if(nums[k] < nums[k+1]){
                break;      // e.g. [1 2 3 9 8 7], k = 2, point to 3
            }
        }
        if(k < 0){
            reverse(nums.begin(), nums.end());  // e.g. [3,2,1] to [1,2,3]
        }else{
            for(l = n - 1; l > k; --l){
                if(nums[l] > nums[k]){
                    break;      // let l point the first larger than nums[k]'s number counting from back
                }
            }
            swap(nums[k], nums[l]);
            reverse(nums.begin()+k+1, nums.end());
        }
    }
};
```

```python
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        p = length - 1

        # e.g. 127431 p point to 7
        while p > 0 and nums[p-1] >= nums[p]:
            p -= 1
        
        # from 127431 to 121347
        reverse_len = length - p
        for i in range(reverse_len // 2):
            nums[p+i], nums[length-1-i] = nums[length-1-i], nums[p+i]
        
        if p > 0:
            for i in range(p, length):
                if nums[i] > nums[p-1]:
                    nums[i], nums[p-1] = nums[p-1], nums[i]
                    break
```