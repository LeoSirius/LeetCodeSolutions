from threading import main_thread
from typing import *

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        max_plus_one = 10 ** n
        return [i for i in range(1, max_plus_one)]


def test(test_name, n, expected):
    res = Solution().printNumbers(n)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    n1 = 1
    expected1 = [1,2,3,4,5,6,7,8,9]
    test('test1', n1, expected1)


# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。
# 比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

# 示例 1:

# 输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
#  

# 说明：

# 用返回一个整数列表来代替打印
# n 为正整数
