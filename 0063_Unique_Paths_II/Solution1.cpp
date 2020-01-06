#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<long long>> dp(m+1, vector<long long>(n+1,0));
        dp[1][0] = 1;
        for (int i = 1 ; i <= m ; ++i)
            for (int j = 1 ; j <= n ; ++j)
                if (!obstacleGrid[i-1][j-1])
                    dp[i][j] = dp[i-1][j]+dp[i][j-1];
        return dp[m][n];
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


