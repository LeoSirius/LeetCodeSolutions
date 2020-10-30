from typing import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if not m:
            return False
        n = len(board[0])
        if not n:
            return False

        def dfs(x, y, p):
            if x < 0 or y < 0 or x >= m or y >= n or board[x][y] != word[p]:
                return False
            if p == len(word) - 1:
                return True

            tmp_char = board[x][y]
            board[x][y] = '.'

            res = dfs(x+1, y, p+1) or dfs(x-1, y, p+1) or dfs(x, y+1, p+1) or dfs(x, y-1, p+1)

            board[x][y] = tmp_char
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        
        return False


def test(test_name, board, word, expected):
    res = Solution().exist(board, word)
    print('res = {}'.format(res))
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    board1 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word1 = 'ABCCED'
    expected1 = True
    test('test1', board1, word1, expected1)

    board2 = [
        ["a","b"],
        ["c","d"]
    ]
    word2 = 'abcd'
    expected2 = False
    test('test2', board2, word2, expected2)

