#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int used_rows[9][9] = {0};                      // 第一维是索引，第二维是数字减1
        int used_cols[9][9] = {0};
        int used_squares[9][9] = {0};
        for (int i = 0; i < board.size(); i++)
        for (int j = 0; j < board[0].size(); j++) {
            if (board[i][j] != '.') {
                int k = i / 3 * 3 + j / 3;              // 把9个小方块分别归入0-8中
                int num = board[i][j] - '0' - 1;        // 下标是0-8
                if (used_rows[i][num] || used_cols[j][num] || used_squares[k][num])
                    return false;
                used_rows[i][num] = used_cols[j][num] = used_squares[k][num] = 1;
            }
        }
        return true;
    }
};


void test(string test_name, vector<vector<char>> &board, bool expected)
{
    Solution s;
    if (s.isValidSudoku(board) == expected) {
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
    bool expected1 = true;
    test("test1", board1, expected1);

    vector<vector<char>> board2 = {
        {'8','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };
    bool expected2 = false;
    test("test2", board2, expected2);

    return 0;
}
