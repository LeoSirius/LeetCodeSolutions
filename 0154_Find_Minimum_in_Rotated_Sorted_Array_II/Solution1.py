from typing import *

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers) - 1
        while l < r:
            mid = l + (r - l) // 2
            if numbers[mid] < numbers[r]:   # e.g.   6712345  mid = 2
                r = mid
            elif numbers[r] < numbers[mid]: # e.g.   3456712  mid = 6
                l = mid + 1
            else:
                # mid == r  e.g.     6711111  mid = 1
                r -= 1
        return numbers[l]


def test(test_name, numbers, expected):
    res = Solution().minArray(numbers)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == '__main__':
    numbers1 = [3,4,5,1,2]
    expected1 = 1
    test('test1', numbers1, expected1)

    numbers2 = [2,2,2,0,1]
    expected2 = 0
    test('test2', numbers2, expected2)



# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
