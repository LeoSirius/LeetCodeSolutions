from typing import *


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []

        def count_one(n):
            cnt = 0
            for i in range(6):
                cnt += n & 1
                n //= 2
            return cnt

        for h in range(12):
            one1 = count_one(h)
            for m in range(60):
                one2 = count_one(m)
                if one1 + one2 == turnedOn:
                    res.append(f'{h}:0{m}' if m < 10 else f'{h}:{m}')

        return res


def test(test_name, turnedOn, expected):
    res = Solution().readBinaryWatch(turnedOn)
    res.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    turnedOn1 = 1
    expected1 = ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
    test('test1', turnedOn1, expected1)

    turnedOn2 = 9
    expected2 = []
    test('test2', turnedOn2, expected2)
