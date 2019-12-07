#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<unsigned int>> dp(m, vector<unsigned int>(n, 0));
        for (int i = 0; i < m; i++) {
            if (!obstacleGrid[i][0]) 
                dp[i][0] = 1;
            else 
                break;
        }
        for (int j = 0; j < n; j++) {
            if (!obstacleGrid[0][j])
                dp[0][j] = 1;
            else
                break;
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!obstacleGrid[i][j] && i > 0 && j > 0) {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
                if (obstacleGrid[i][j]) {
                    dp[i][j] = 0;
                }
            }
        }
        return dp[m-1][n-1];
    }
};

void test(string test_name, vector<vector<int>> &obstacleGrid, int expected)
{
    Solution s;
    if (s.uniquePathsWithObstacles(obstacleGrid) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<int>> obstacleGrid1 = {
        {0,0,0},
        {0,1,0},
        {0,0,0}
    };
    int expected1 = 2;
    test("test1", obstacleGrid1, expected1);

    vector<vector<int>> obstacleGrid2 = {{1}};
    int expected2 = 0;
    test("test2", obstacleGrid2, expected2);

    vector<vector<int>> obstacleGrid3 = {{1, 0}};
    int expected3 = 0;
    test("test3", obstacleGrid3, expected3);

    return 0;
}


