#include <iostream>
#include <vector>
using namespace std;

class Solution {
    void dfs(vector<vector<char>>& board, int i, int j)
    {
        if (i < 0 || j < 0 || board.size() <= i || board[0].size() <= j || board[i][j] != 'O')
            return;
        board[i][j] = '-';
        dfs(board, i + 1, j);
        dfs(board, i - 1, j);
        dfs(board, i, j + 1);
        dfs(board, i, j - 1);
    }
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        if (!m) return;
        int n = board[0].size();
        if (!n) return;

        for (int i = 0; i < m; i++) {
            dfs(board, i, 0);
            dfs(board, i, n - 1);
        }

        for (int j = 0; j < n; j++) {
            dfs(board, 0, j);
            dfs(board, m - 1, j);
        }

        for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            // 注意这里必须是先把O变成X，顺序不能变
            if (board[i][j] == 'O') board[i][j] = 'X';
            if (board[i][j] == '-') board[i][j] = 'O';
        }
    }
};

void test(string test_name, vector<vector<char>> board, vector<vector<char>> expected)
{
    Solution().solve(board);
    if (board == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<vector<char>> board1 = {
        {'X', 'X', 'X', 'X'},
        {'X', 'O', 'O', 'X'},
        {'X', 'X', 'O', 'X'},
        {'X', 'O', 'X', 'X'},
    };
    vector<vector<char>> expected1 = {
        {'X', 'X', 'X', 'X'},
        {'X', 'X', 'X', 'X'},
        {'X', 'X', 'X', 'X'},
        {'X', 'O', 'X', 'X'},
    };
    test("test1", board1, expected1);

    return 0;
}

// Given a 2D board containing 'X' and 'O' (the letter O), 
// capture all regions surrounded by 'X'.

// A region is captured by flipping all 'O's into 'X's in that surrounded region.

// Example:

// X X X X
// X O O X
// X X O X
// X O X X

// After running your function, the board should be:

// X X X X
// X X X X
// X X X X
// X O X X

// Explanation:

// Surrounded regions shouldn’t be on the border, which means that any 'O' 
// on the border of the board are not flipped to 'X'. Any 'O' that is not on
//  the border and it is not connected to an 'O' on the border will be flipped 
// to 'X'. Two cells are connected if they are adjacent cells connected 
// horizontally or vertically.
