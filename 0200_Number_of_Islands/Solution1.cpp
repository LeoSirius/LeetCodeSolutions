#include <iostream>
#include <vector>
using namespace std;

class Solution {
    void dfs_infect(vector<vector<char>>& grid, int x, int y)
    {
        if (x < 0 || y < 0 || grid.size() <= x || grid[0].size() <= y || grid[x][y] != '1')
            return;
        
        grid[x][y] = '2';
        dfs_infect(grid, x+1, y);
        dfs_infect(grid, x-1, y);
        dfs_infect(grid, x, y+1);
        dfs_infect(grid, x, y-1);
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;

        int m = grid.size();
        if (!m) return res;
        int n = grid[0].size();
        if (!n) return res;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    res++;
                    dfs_infect(grid, i, j);
                }
            }
        }
        return res;
    }
};

void test(string test_name, vector<vector<char>>& grid, int expected)
{
    int res = Solution().numIslands(grid);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<vector<char>> grid1 = {
        {'1','1','1','1','0'},
        {'1','1','0','1','0'},
        {'1','1','0','0','0'},
        {'0','0','0','0','0'},
    };
    int expected1 = 1;
    test("test1", grid1, expected1);

    vector<vector<char>> grid2 = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'},
    };
    int expected2 = 3;
    test("test2", grid2, expected2);

    return 0;
}


// Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
// An island is surrounded by water and is formed by connecting adjacent lands 
// horizontally or vertically. You may assume all four edges of the grid are all 
// surrounded by water.

// Example 1:
// Input:
// 11110
// 11010
// 11000
// 00000

// Output: 1


// Example 2:
// Input:
// 11000
// 11000
// 00100
// 00011

// Output: 3

