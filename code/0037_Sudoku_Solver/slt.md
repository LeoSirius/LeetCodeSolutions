### 思路1 回溯法

DFS与回溯法的区别：（简单来说就是DFS是回溯法的一种）

- Backtracking is a more general purpose algorithm.
- Depth-First search is a specific form of backtracking related to searching tree structures.

回溯法（探索与回溯法）是一种选优搜索法，又称为试探法，按选优条件向前搜索，以达到目标。 但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点”。回溯法是暴力搜索法中的一种。

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def find_uassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.find_uassigned()
        # no dot in board, all solved
        if (row, col) == (-1, -1):
            return True

        # backtracking every number, in every possible position
        for num in ['1','2','3','4','5','6','7','8','9']:
            if self.is_safe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '.'
        return False

    def is_safe(self, row, col, ch):
        # left-top index of every square
        boxrow = row - row % 3
        boxcol = col - col % 3
        if self.check_row(row, ch) and self.check_col(col, ch) and self.check_square(boxrow, boxcol, ch):
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

    def check_square(self, row, col, ch):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.board[r][c] == ch:
                    return False
        return True
```