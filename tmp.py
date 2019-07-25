class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def find_ussigned(self)
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == '.':
                    return r, c
        return -1, -1

    def solve(self):
        row, col = self.find_ussigned()
        if (row, col) == (-1, -1):
            return True
        
        for num in ['1','2','3','4','5','6','7','8','9']:
            if self.is_safe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '.'
        return False

    def is_safe(self, row, col, ch):
        box_row = row - row % 3
        box_col = col - col % 3
        if self.check_row(row, ch) and self.check_col(col, ch) and self.check_square(box_row, box_col, ch):
            return True
        return False
        
    def check_row(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True
    
    def check_col(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True
    
    def check_square(self, box_row, box_col, ch):
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if self.board[r][c] == ch:
                    return False
        return True