from typing import *


class Solution:
    def printKMoves(self, K: int) -> List[str]:
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]        # represents 'L', 'U'
        black = set()
        pos, curr_dir = (0, 0), 2

        # simulate K moves
        for i in range(K):
            if pos in black:
                curr_dir = (curr_dir - 1) % 4
                black.remove(pos)
            else:
                curr_dir = (curr_dir + 1) % 4
                black.add(pos)
            pos = (pos[0] + dirs[curr_dir][0], pos[1] + dirs[curr_dir][1])

        all_x = [x for x, _ in black] + [pos[0]]
        all_y = [y for _, y in black] + [pos[1]]
        min_x, max_x, min_y, max_y = min(all_x), max(all_x), min(all_y), max(all_y)

        # init all square to white
        matrix = [['_' for _ in range(min_y, max_y + 1)] for _ in range(min_x, max_x + 1)]

        # draw black
        for x, y in black:
            matrix[x - min_x][y - min_y] = 'X'

        # draw direction
        matrix[pos[0]-min_x][pos[1]-min_y] = ['L', 'U', 'R', 'D'][curr_dir]

        for i in range(len(matrix)):
            matrix[i] = ''.join(matrix[i])

        return matrix


def test(test_name, K, expected):
    res = Solution().printKMoves(K)
    print(f'res = {res}')
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    K1 = 0
    expected1 = [
        'R',
    ]
    test('test1', K1, expected1)

    K2 = 2
    expected2 = [
        '_X',
        'LX',
    ]
    test('test2', K2, expected2)

    K3 = 5
    expected3 = [
        '_U',
        'X_',
        'XX',
    ]
    test('test3', K3, expected3)

# An ant is sitting on an infinite grid of white and black squares. It initially faces right. All squares are white initially.

# At each step, it does the following:

# (1) At a white square, flip the color of the square, turn 90 degrees right (clockwise), and move forward one unit.

# (2) At a black square, flip the color of the square, turn 90 degrees left (counter-clockwise), and move forward one unit.

# Write a program to simulate the first K moves that the ant makes and print the final board as a grid.

# The grid should be represented as an array of strings, where each element represents one row in the grid. The black square is represented as 'X', and the white square is represented as '_', the square which is occupied by the ant is represented as 'L', 'U', 'R', 'D', which means the left, up, right and down orientations respectively. You only need to return the minimum matrix that is able to contain all squares that are passed through by the ant.

# Example 1:
# Input: 0
# Output: ["R"]

# Example 2:
# Input: 2
# Output:
# [
#   "_X",
#   "LX"
# ]

# Example 3:
# Input: 5
# Output:
# [
#   "_U",
#   "X_",
#   "XX"
# ]
# Note:

# K <= 100000

