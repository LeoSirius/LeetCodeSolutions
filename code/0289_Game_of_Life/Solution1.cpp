#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        int n = m ? board[0].size() : 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int count = 0;
                for (int x = max(i-1, 0); x <= min(i+1, m-1); ++x)
                    for (int y = max(j-1, 0); y <= min(j+1, n-1); ++y)
                        count += board[x][y] & 1;
                if (count == 3 || (count == 4 && board[i][j] == 1))
                    board[i][j] |= 2;
            }
        }
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                board[i][j] >>= 1;
    }
};

void test(string test_name, vector<vector<int>>& board, vector<vector<int>>& expected)
{
    Solution().gameOfLife(board);
    if (board == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<int>> board1 = {
        {0,1,0},
        {0,0,1},
        {1,1,1},
        {0,0,0}
    };
    vector<vector<int>> expected1 = {
        {0,0,0},
        {1,0,1},
        {0,1,1},
        {0,1,0}
    };
    test("test1", board1, expected1);

    return 0;
}
