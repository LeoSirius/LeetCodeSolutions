#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxValue(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();

        // 初始化第一行和第一列
        for (int j = 1; j < n; j++)
            grid[0][j] += grid[0][j-1];
        for (int i = 1; i < m; i++)
            grid[i][0] += grid[i-1][0];

        for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            grid[i][j] += max(grid[i][j-1], grid[i-1][j]);

        return grid.back().back();
    }
};

void test(string test_name, vector<vector<int>>& grid, int expected)
{
    int res = Solution().maxValue(grid);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<vector<int>> grid1 = {
        {1,3,1},
        {1,5,1},
        {4,2,1}
    };
    int expected1 = 12;
    test("test1", grid1, expected1);

    return 0;
}

// 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
// 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
// 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

// 示例 1:
// 输入: 
// [
//   [1,3,1],
//   [1,5,1],
//   [4,2,1]
// ]
// 输出: 12

// 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
//  
// 提示：
// 0 < grid.length <= 200
// 0 < grid[0].length <= 200
