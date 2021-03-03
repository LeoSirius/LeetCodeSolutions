from typing import *


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            if i % 2 == 0:
                res.append(res[i//2])
            else:
                res.append(res[-1] + 1)

        return res


def test(test_name, num, expected):
    res = Solution().countBits(num)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    num1 = 2
    expected1 = [0,1,1]
    test('test1', num1, expected1)

    num2 = 5
    expected2 = [0,1,1,2,1,2]
    test('test2', num2, expected2)

