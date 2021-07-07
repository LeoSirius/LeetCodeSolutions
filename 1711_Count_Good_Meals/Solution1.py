from typing import *
from collections import defaultdict

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mapper = defaultdict(int)
        MOD = 10 ** 9 + 7
        res = 0

        for n in deliciousness:
            power_of_2 = 1
            for i in range(22):
                n2find = power_of_2 - n
                if n2find >= 0 and n2find in mapper:
                    # 如果 n + n2find == power_of_2
                    # 则把 n2find 之前出现过的总次数加到 res
                    res += mapper[n2find]
                power_of_2 *= 2
            mapper[n] += 1

        return res % MOD


def test(test_name, deliciousness, expected):
    res = Solution().countPairs(deliciousness)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    deliciousness1 = [1,3,5,7,9]
    expected1 = 4
    test('test1', deliciousness1, expected1)

    deliciousness2 = [1,1,1,3,3,3,7]
    expected2 = 15
    test('test2', deliciousness2, expected2)

    deliciousness3 = [2160,1936,3,29,27,5,2503,1593,2,0,16,0,3860,28908,6,2,15,49,6246,1946,23,105,7996,196,0,2,55,457,5,3,924,7268,16,48,4,0,12,116,2628,1468]
    expected3 = 53
    test('test3', deliciousness3, expected3)
