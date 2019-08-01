### 思路1 回溯法

DFS与回溯法的区别：

- Backtracking is a more general purpose algorithm.
- Depth-First search is a specific form of backtracking related to searching tree structures.

回溯法（探索与回溯法）是一种选优搜索法，又称为试探法，按选优条件向前搜索，以达到目标。 但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点”。回溯法是暴力搜索法中的一种。

```cpp
class Solution {
    bool check(vector<vector<char>>& board, int row, int col, char val){
        int boxrow = row - row % 3;  // boxrow, boxcol 是每个小正方形最左上角的索引
        int boxcol = col - col % 3;
        for(int x = 0; x < 9; ++x) if(board[x][col] == val) return false;
        for(int y = 0; y < 9; ++y) if(board[row][y] == val) return false;
        for(int x = 0; x < 3; ++x)
        for(int y = 0; y < 3; ++y)
            if(board[boxrow+x][boxcol+y] == val) return false;
        return true;
    }
    // 以递归的方式遍历了每个方格
    bool solveSudoku(vector<vector<char>>& board, int row, int col){
        if(row == 9) return true;
        if(col == 9) return solveSudoku(board, row+1, 0);
        if(board[row][col] != '.') return solveSudoku(board, row, col+1);

        for(char c = '1'; c <= '9'; ++c){
            if(check(board, row, col, c)){
                board[row][col] = c;
                if(solveSudoku(board, row, col+1)) return true;
                board[row][col] = '.';
            }
        }
        return false;
    }
public:
    void solveSudoku(vector<vector<char>>& board) {
        solveSudoku(board, 0, 0);
    }
};
```

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