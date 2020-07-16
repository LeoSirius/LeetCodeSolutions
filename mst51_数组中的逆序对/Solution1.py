from typing import *

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.res = 0
        
        def merge(nums, tmp, l, mid, r):
            pl, pr = l, mid + 1
            while pl <= mid and pr <= r:
                # l到mid和mid+1到r都是内部有序的
                # [pl,mid+1]中的数都比pr大，即这些都是逆序
                # 把一个后半的比pl小的数放到pl前面，[pl,mid+1]这些逆序就消灭了
                if nums[pr] < nums[pl]:
                    self.res += mid + 1 - pl
                    tmp.append(nums[pr])
                    pr += 1
                else:
                    tmp.append(nums[pl])
                    pl += 1
            while pl <= mid:
                tmp.append(nums[pl])
                pl += 1
            while pr <= r:
                tmp.append(nums[pr])
                pr += 1
            
            for i in range(len(tmp)):
                nums[l + i] = tmp[i]
            tmp.clear()

        def merge_sort(nums, tmp, l, r):
            if l >= r: return
            mid = l + ((r - l) >> 1)
            merge_sort(nums, tmp, l, mid)
            merge_sort(nums, tmp, mid+1, r)
            merge(nums, tmp, l, mid, r)
        
        merge_sort(nums, [], 0, len(nums)-1)
        return self.res


def test(test_name, nums, expected):
    res = Solution().reversePairs(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed')


if __name__ == "__main__":
    nums1 = [7,5,6,4]
    expected1 = 5
    test('test1', nums1, expected1)

    nums2 = [1,3,2,3,1]
    expected2 = 4
    test('test2', nums2, expected2)



# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组，求出这个数组中的逆序对的总数。

# 示例 1:
# 输入: [7,5,6,4]
# 输出: 5
#  

# 限制：
# 0 <= 数组长度 <= 50000
