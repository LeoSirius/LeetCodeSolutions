from typing import *


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        size = len(row)

        res = 0
        for i in range(0, size - 1, 2):
            if row[i] == row[i+1] ^ 1:
                continue
            for j in range(i + 1, size):
                if row[i] == row[j] ^ 1:
                    row[i + 1], row[j] = row[j], row[i + 1]
                    res += 1
                    break

        return res


def test(test_name, row, expected):
    res = Solution().minSwapsCouples(row)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    row1 = [0, 2, 1, 3]
    expected1 = 1
    test('test1', row1, expected1)

    row2 = [3, 2, 0, 1]
    expected2 = 0
    test('test2', row2, expected2)


# N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

# The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

# The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

# Example 1:

# Input: row = [0, 2, 1, 3]
# Output: 1
# Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

# Example 2:

# Input: row = [3, 2, 0, 1]
# Output: 0
# Explanation: All couples are already seated side by side.
# Note:

# len(row) is even and in the range of [4, 60].
# row is guaranteed to be a permutation of 0...len(row)-1.

