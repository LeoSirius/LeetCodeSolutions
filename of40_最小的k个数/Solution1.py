from typing import *

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

def test(test_name, arr, k, expected_list):
    res = Solution().getLeastNumbers(arr, k)
    if res in expected_list:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    arr1 = [3,2,1]
    k1 = 2
    expected_list1 = [[1,2],[2,1]]
    test('test1', arr1, k1, expected_list1)

    arr2 = [0,1,2,1]
    k2 = 1
    expected_list2 = [[0]]
    test('test2', arr2, k2, expected_list2)


# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，
# 则最小的4个数字是1、2、3、4。

# 示例 1：
# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]

# 示例 2：
# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]

# 限制：
# 0 <= k <= arr.length <= 10000
# 0 <= arr[i] <= 10000

