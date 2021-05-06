from typing import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res

        for i in range(numRows - 1):
            last_row = res[-1]
            new_row = [1] * (len(last_row) + 1)

            for i in range(1, len(last_row)):
                new_row[i] = last_row[i] + last_row[i-1]
            res.append(new_row)

        return res


def test(test_name, numRows, expected):
    res = Solution().generate(numRows)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    numRows1 = 5
    expected1 = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    test('test1', numRows1, expected1)

    numRows2 = 1
    expected2 = [[1]]
    test('test2', numRows2, expected2)
