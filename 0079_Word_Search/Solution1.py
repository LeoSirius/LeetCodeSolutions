from typing import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def is_found(x, y, word_p):
            if (x < 0 or
                m <= x or
                y < 0 or
                n <= y or
                word_p == len(word) or
                board[x][y] != word[word_p]):
                return False
            if word_p == len(word) - 1:
                return True
            tmp = board[x][y]
            board[x][y] = '*'  # 用一个特殊的字符来污染走过的路
            if (is_found(x+1, y, word_p+1) or
                is_found(x-1, y, word_p+1) or
                is_found(x, y+1, word_p+1) or
                is_found(x, y-1, word_p+1)):
                return True
            board[x][y] = tmp

        for i in range(m):
            for j in range(n):
                if is_found(i, j, 0):
                    return True
        return False

def test(test_name, board, word, expected):
    res = Solution().exist(board, word)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')



if __name__ == "__main__":
    board1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ];
    word1 = "ABCCED";
    expected1 = True;
    test("test1", board1, word1, expected1);

    board2 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ];
    word2 = "SEE";
    expected2 = True;
    test("test2", board2, word2, expected2);

    board3 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ];
    word3 = "ABCB";
    expected3 = False;
    test("test3", board3, word3, expected3);


# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell,
#  where "adjacent" cells are those horizontally or vertically neighboring.
#   The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#  
# Constraints:

# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
