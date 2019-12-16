#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {

        int m = grid.size();
        int n = grid[0].size();
        vector<int> dp(n, grid[0][0]);
        // 第一行
        for (int i = 1; i < n; i++) {
            dp[i] = dp[i-1] + grid[0][i];
        }
        for (int i = 1; i < m; i++) {
            dp[0] += grid[i][0];
            for (int j = 1; j < n; j++) {
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j];
            }
        }
        return dp[n-1];
    }
};

void test(string test_name, vector<vector<int>> &grid, int expected)
{
    Solution s;
    if (s.minPathSum(grid) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<int>> grid1 = {
        {1,3,1},
        {1,5,1},
        {4,2,1},
    };
    int expected1 = 7;
    test("test1", grid1, expected1);

    return 0;
}
