#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0)
            return matrix;
        int n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        int area = m * n;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (matrix[i][j] == 0)
                    dp[i][j] = 0;
                else {
                    int up = i > 0 ? dp[i-1][j] : area;
                    int left = j > 0 ? dp[i][j-1] : area;
                    dp[i][j] = min(up, left) + 1;
                }

        for (int i = m - 1; i >= 0; --i)
            for (int j = n - 1; j >= 0; --j)
                if (matrix[i][j] == 0)
                    dp[i][j] = 0;
                else {
                    int down = i < m - 1 ? dp[i+1][j] : area;
                    int right = j < n - 1 ? dp[i][j+1] : area;
                    dp[i][j] = min(min(down, right) + 1, dp[i][j]);
                }
        return dp;
    }
};

void test(string test_name, vector<vector<int>>& matrix, vector<vector<int>>& expected)
{
    vector<vector<int>> res = Solution().updateMatrix(matrix);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<vector<int>> matrix1 = {
        {0,0,0},
        {0,1,0},
        {0,0,0}
    };
    vector<vector<int>> expected1 = {
        {0,0,0},
        {0,1,0},
        {0,0,0}
    };
    test("test1", matrix1, expected1);

    vector<vector<int>> matrix2 = {
        {0,0,0},
        {0,1,0},
        {1,1,1}
    };
    vector<vector<int>> expected2 = {
        {0,0,0},
        {0,1,0},
        {1,2,1}
    };
    test("test2", matrix2, expected2);

    vector<vector<int>> matrix3 = {
        {1,0,1,1,0,0,1,0,0,1},
        {0,1,1,0,1,0,1,0,1,1},
        {0,0,1,0,1,0,0,1,0,0},
        {1,0,1,0,1,1,1,1,1,1},
        {0,1,0,1,1,0,0,0,0,1},
        {0,0,1,0,1,1,1,0,1,0},
        {0,1,0,1,0,1,0,0,1,1},
        {1,0,0,0,1,1,1,1,0,1},
        {1,1,1,1,1,1,1,0,1,0},
        {1,1,1,1,0,1,0,0,1,1}
    };
    vector<vector<int>> expected3 = {
        {1,0,1,1,0,0,1,0,0,1},
        {0,1,1,0,1,0,1,0,1,1},
        {0,0,1,0,1,0,0,1,0,0},
        {1,0,1,0,1,1,1,1,1,1},
        {0,1,0,1,1,0,0,0,0,1},
        {0,0,1,0,1,1,1,0,1,0},
        {0,1,0,1,0,1,0,0,1,1},
        {1,0,0,0,1,2,1,1,0,1},
        {2,1,1,1,1,2,1,0,1,0},
        {3,2,2,1,0,1,0,0,1,1}
    };
    test("test3", matrix3, expected3);

    return 0;
}
