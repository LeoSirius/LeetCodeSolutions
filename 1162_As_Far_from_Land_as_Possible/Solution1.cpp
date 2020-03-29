#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        if (grid.empty())
            return -1;

        int size = grid.size();
        queue<pair<int, int>> q;
        for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++) {
            if (grid[i][j] == 1) {
                grid[i][j] = -1;
                q.push({i, j});
            }
        }

        int dist = 1;
        int level_len = q.size();
        while (!q.empty()) {
            auto cell = q.front(); q.pop();
            level_len--;

            int i = cell.first, j = cell.second;

            if (i > 0 && grid[i-1][j] == 0) {
                q.push({i-1, j});
                grid[i-1][j] = dist;
            }
            if (j > 0 && grid[i][j-1] == 0) {
                q.push({i, j-1});
                grid[i][j-1] = dist;
            }
            if (i < size - 1 && grid[i+1][j] == 0) {
                q.push({i+1, j});
                grid[i+1][j] = dist;
            }
            if (j < size - 1 && grid[i][j+1] == 0) {
                q.push({i, j+1});
                grid[i][j+1] = dist;
            }
            if (level_len == 0) {
                level_len = q.size();
                dist++;
            }
        }

        int res = 0;
        for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            res = max(res, grid[i][j]);

        // 没有陆地或没有海洋，res = 0， 按题意应该返回-1
        return res == 0 ? -1 : res;
    }
};

void test(string test_name, vector<vector<int>>& grid, int expected)
{
    int res = Solution().maxDistance(grid);
    if (res == expected) {
        cout << test_name + " success." << endl;
    } else {
        cout << test_name + " failed." << endl;
    }
}

int main()
{
    vector<vector<int>> grid1 = {{1,0,1},{0,0,0},{1,0,1}};
    int expected1 = 2;
    test("test1", grid1, expected1);

    vector<vector<int>> grid2 = {{1,0,0},{0,0,0},{0,0,0}};
    int expected2 = 4;
    test("test2", grid2, expected2);

    vector<vector<int>> grid3 = {{0,0,0,0,}, {0,0,0,0},{0,0,0,0},{0,0,0,0}};
    int expected3 = -1;
    test("test3", grid3, expected3);

    return 0;
}