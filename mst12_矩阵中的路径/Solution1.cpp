#include <iostream>
#include <vector>
using namespace std;

class Solution {
    bool dfs(vector<vector<char>>& board, int x, int y, int p, string word)
    {
        if (x < 0 || board.size() <= x || y < 0 || board[0].size() <= y || board[x][y] != word[p])
            return false;
        if (p == word.size() - 1)
            return true;
        char tmp = board[x][y];
        board[x][y] = '.';      // 标记当前元素，word中的单词肯定不等于'.'。避免重复
        bool res = dfs(board, x+1, y, p+1, word) ||
                dfs(board, x-1, y, p+1, word) ||
                dfs(board, x, y+1, p+1, word) ||
                dfs(board, x, y-1, p+1, word);
        board[x][y] = tmp;
        return res;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        for (int i = 0; i < board.size(); i++)
        for (int j = 0; j < board[0].size(); j++)
            if (dfs(board, i, j, 0, word))
                return true;
        return false;
    }
};


void test(string test_name, vector<vector<char>>& board, string word, bool expected)
{
    bool res = Solution().exist(board, word);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<vector<char>> board1 = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    string word1 = "ABCCED";
    bool expected1 = true;
    test("test1", board1, word1, expected1);

    vector<vector<char>> board2 = {
        {'a','b'},
        {'c','d'}
    };
    string word2 = "abcd";
    bool expected2 = false;
    test("test2", board2, word2, expected2);
}

