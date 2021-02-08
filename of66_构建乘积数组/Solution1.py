from typing import *

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        a_len = len(a)
        res = [1 for _ in range(a_len)]

        cur_mul = 1
        for i in range(a_len):
            res[i] *= cur_mul
            cur_mul *= a[i]

        cur_mul = 1
        for i in range(a_len-1, -1, -1):
            res[i] *= cur_mul
            cur_mul *= a[i]

        return res


def test(test_name, a, expected):
    res = Solution().constructArr(a)
    print(res)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    a1 = [1,2,3,4,5]
    expected1 = [120,60,40,30,24]
    test('test1', a1, expected1)


# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
# 其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。


# 示例:

# 输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24]


# 提示：

# 所有元素乘积之和不会溢出 32 位整数
# a.length <= 100000
