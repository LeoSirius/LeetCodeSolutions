#include <iostream>
#include <vector>
using namespace std;

class Solution {
    int res = 0;
    bool is_valid(vector<string>& board, int row, int col)
    {
        for (int i = 0; i < row; ++i) {
            if (board[i][col] == 'Q') return false;
        }
        for (int i = row - 1, j = col - 1; i >= 0; --i, --j) {
            if (board[i][j] == 'Q') return false;
        }
        for (int i = row - 1, j = col + 1; i >= 0; --i, ++j) {
            if (board[i][j] == 'Q') return false;
        }
        return true;
    }

    void traceback(vector<string>& board, int row)
    {
        if (row == board.size()) {
            ++res;
            return;
        }
        int col_num = board[0].size();

        for (int col = 0; col < col_num; ++col) {
            if (is_valid(board, row, col)) {
                board[row][col] = 'Q';
                traceback(board, row + 1);
                board[row][col] = '.';
            }
        }
    }
public:
    int totalNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        traceback(board, 0);
        return res;
    }
};

void test(string test_name, int n, int expected)
{
    int res = Solution().totalNQueens(n);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 4;
    int expected1 = 2;
    test("test1", n1, expected1);

    return 0;
}