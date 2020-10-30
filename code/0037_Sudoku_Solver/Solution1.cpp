#include <iostream>
#include <vector>
using namespace std;

class Solution {

    bool check(vector<vector<char>>& board, int row, int col ,char ch)
    {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == ch || board[i][col] == ch)
                return false;
        }
        // col % 3 后就是 col在左上开始后的索引，然后col再减col % 3，便回到了左上方
        // boxrow, boxcol 是每个小正方形最左上角的索引
        int box_row = row - row % 3;
        int box_col = col - col % 3;
        for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[box_row + i][box_col + j] == ch)
                return false;
        return true;
    }

    bool solved(vector<vector<char>>& board, int row, int col)
    {
        // 以递归的方式遍历了每个方格
        if (row == 9)
            return true;
        if (col == 9)
            return solved(board, row + 1, 0);
        if (board[row][col] != '.')
            return solved(board, row, col + 1);

        for (char ch = '1'; ch <= '9'; ch++) {
            if (check(board, row, col, ch)) {
                board[row][col] = ch;
                if (solved(board, row, col + 1))
                    return true;
                board[row][col] = '.';
            }
        }
        return false;
    }
public:
    void solveSudoku(vector<vector<char>>& board) {
        solved(board, 0, 0);
    }
};


void test(string test_name, vector<vector<char>> board, vector<vector<char>> &expected)
{
    Solution().solveSudoku(board);
    if (board == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<char>> board1 = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'},
    };
    vector<vector<char>> expected1 = {
        {'5','3','4','6','7','8','9','1','2'},
        {'6','7','2','1','9','5','3','4','8'},
        {'1','9','8','3','4','2','5','6','7'},
        {'8','5','9','7','6','1','4','2','3'},
        {'4','2','6','8','5','3','7','9','1'},
        {'7','1','3','9','2','4','8','5','6'},
        {'9','6','1','5','3','7','2','8','4'},
        {'2','8','7','4','1','9','6','3','5'},
        {'3','4','5','2','8','6','1','7','9'},
    };
    test("test1", board1, expected1);

    return 0;
}
