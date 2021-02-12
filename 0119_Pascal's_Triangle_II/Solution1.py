from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            new_row = [1]
            for j in range(1, len(res)):
                new_row.append(res[j-1] + res[j])
            new_row.append(1)
            res = new_row

        return res


def test(test_name, rowIndex, expected):
    res = Solution().getRow(rowIndex)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    rowIndex1 = 3
    expected1 = [1,3,3,1]
    test('test1', rowIndex1, expected1)

    rowIndex2 = 0
    expected2 = [1]
    test('test2', rowIndex2, expected2)

    rowIndex3 = 1
    expected3 = [1,1]
    test('test3', rowIndex3, expected3)


#Example 1:
#Input: rowIndex = 3
#Output: [1,3,3,1]
#
#Example 2:
#Input: rowIndex = 0
#Output: [1]
#
#Example 3:
#Input: rowIndex = 1
#Output: [1,1]
# 
#
#Constraints:
#
#0 <= rowIndex <= 33

