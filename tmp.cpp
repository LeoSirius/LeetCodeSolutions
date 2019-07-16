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