class Solution:
    def isValidSudoku(self, board) -> bool:
        for row in board:
            print(row)
        used_row = used_col = used_square = [[0] * 9] * 9
        for row in used_row:
            print(row)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('0') - 1
                    k = i // 3 * 3 + j // 3
                    if used_row[i][num] or used_col[j][num] or used_square[k][num]:
                        return False
                    used_row[i][num] = used_col[j][num] = used_square[k][num] = 1
        return True

input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s = Solution()
print('res = ' + str(s.isValidSudoku(input)))
