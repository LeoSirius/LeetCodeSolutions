from typing import *


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row_presum = []
        for row in matrix:
            presum = [row[0]]
            for i in range(1, len(row)):
                presum.append(row[i] + presum[-1])
            self.row_presum.append(presum)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            if col1 == 0:
                cur = self.row_presum[row][col2]
            else:
                cur = self.row_presum[row][col2] - self.row_presum[row][col1 - 1]
            res += cur
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

def test1():
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    res1 = obj.sumRegion(2, 1, 4, 3)
    res2 = obj.sumRegion(1, 1, 2, 2)
    res3 = obj.sumRegion(1, 2, 2, 4)
    if (res1, res2, res3) == (8, 11, 12):
        print('test1 success.')
    else:
        print('test1 failed.')


if __name__ == '__main__':
    test1()

