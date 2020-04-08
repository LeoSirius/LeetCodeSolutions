#include <iostream>
#include <vector>
using namespace std;

class Solution {
    vector<vector<string>> res;

    bool is_valid(vector<string>& board, int row, int col)
    {
        for (int i = row - 1; i >= 0; --i)
            if (board[i][col] == 'Q')
                return false;
        for (int i = row - 1, j = col - 1; i >= 0; --i, --j)
            if (board[i][j] == 'Q')
                return false;
        for (int i = row - 1, j = col + 1; i >= 0; --i, ++j)
            if (board[i][j] == 'Q')
                return false;
        return true;
    }

    void backtrack(vector<string>& board, int row)
    {
        int n = board.size();
        if (row == n) {
            res.push_back(board);
            return;
        }
        for (int col = 0; col < n; ++col) {
            if (!is_valid(board, row, col))
                continue;
            board[row][col] = 'Q';
            backtrack(board, row + 1);
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


// The n-queens puzzle is the problem of placing n queens on an
//  n×n chessboard such that no two queens attack each other.



// Given an integer n, return all distinct solutions to the n-queens puzzle.

// Each solution contains a distinct board configuration of the n-queens'' placement, 
// where 'Q' and '.' both indicate a queen and an empty space respectively.

// Example:

// Input: 4
// Output: [
//  [".Q..",  // Solution 1
//   "...Q",
//   "Q...",
//   "..Q."],

//  ["..Q.",  // Solution 2
//   "Q...",
//   "...Q",
//   ".Q.."]
// ]
// Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

