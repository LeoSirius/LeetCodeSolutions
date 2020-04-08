#include <iostream>
#include <vector>
using namespace std;

class Solution {
    vector<vector<string>> res;

    bool is_valid(vector<string>& board, int row, int col)
    {
        // 只用检查上面三个方向，因为下面的都是'.'，这一行只有一个Q
        // 检查上方
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q')
                return false;
        }
        // 检查左上方（正方形，ij检查一个就行了）
        for (int i = row - 1, j = col - 1; i >= 0; --i, --j) {
            if (board[i][j] == 'Q')
                return false;
        }
        // 检查右上方
        for (int i = row - 1, j = col + 1; i >= 0; --i, ++j) {
            if (board[i][j] == 'Q')
                return false;
        }
        return true;
    }

    void backtrack(vector<string>& board, int row)
    {
        if (row == board.size()) {
            res.push_back(board);
            return;
        }
        int col_num = board[0].size();
        for (int col = 0; col < col_num; col++) {
            if (!is_valid(board, row, col))
                continue;
            board[row][col] = 'Q';
            backtrack(board, row + 1);   // 一行必然只能有一个Q，所以这里直接跳到下一行了
            board[row][col] = '.';
        }
    }
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        backtrack(board, 0);
        return res;
    }
};

void test(string test_name, int n, vector<vector<string>>& expected)
{
    vector<vector<string>> res = Solution().solveNQueens(n);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 4;
    vector<vector<string>> expected1 = {
        {
            ".Q..",
            "...Q",
            "Q...",
            "..Q."
        },
        {
            "..Q.",
            "Q...",
            "...Q",
            ".Q.."
        }
    };
    test("test1", n1, expected1);

    return 0;
}
