#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        int board_size = board.size();
        int res = 0;

        for (int i = 0; i < board_size; ++i) {
            for (int j = 0; j < board_size; ++j) {
                if (board[i][j] == 'R') {
                    int p = j - 1;
                    while (p >= 0 && board[i][p] == '.') --p;
                    if (p >= 0 && board[i][p] == 'p') {
                        ++res;
                    }

                    p = j + 1;
                    while (p < board_size && board[i][p] == '.') ++p;
                    if (p < board_size && board[i][p] == 'p') {
                        ++res;
                    }

                    p = i - 1;
                    while (p >= 0 && board[p][j] == '.') --p;
                    if (p >= 0 && board[p][j] == 'p') {
                        ++res;
                    }

                    p = i + 1;
                    while (p < board_size && board[p][j] == '.') ++p;
                    if (p < board_size && board[p][j] == 'p')
                        ++res;
                }
            }
        }
        return res;
    }
};

void test(string test_name, vector<vector<char>>& board, int expected)
{
    int res = Solution().numRookCaptures(board);
    if (res == expected) {
        cout << test_name << " succcess." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<char>> board1 = {
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','p','.','.','.','.'},
        {'.','.','.','R','.','.','.','p'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','p','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},{'.','.','.','.','.','.','.','.'}};
    int expected1 = 3;
    test("test1", board1, expected1);

    vector<vector<char>> board2 = {{'.','.','.','.','.','.','.','.'},{'.','p','p','p','p','p','.','.'},{'.','p','p','B','p','p','.','.'},{'.','p','B','R','B','p','.','.'},{'.','p','p','B','p','p','.','.'},{'.','p','p','p','p','p','.','.'},{'.','.','.','.','.','.','.','.'},{'.','.','.','.','.','.','.','.'}};
    int expected2 = 0;
    test("test2", board2, expected2);

    vector<vector<char>> board3 = {{'.','.','.','.','.','.','.','.'},{'.','.','.','p','.','.','.','.'},{'.','.','.','p','.','.','.','.'},{'p','p','.','R','.','p','B','.'},{'.','.','.','.','.','.','.','.'},{'.','.','.','B','.','.','.','.'},{'.','.','.','p','.','.','.','.'},{'.','.','.','.','.','.','.','.'}};
    int expected3 = 3;
    test("test3", board3, expected3);

    vector<vector<char>> board4 = {
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','R','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'}};
    int expected4 = 0;
    test("test4", board4, expected4);

    return 0;
}
