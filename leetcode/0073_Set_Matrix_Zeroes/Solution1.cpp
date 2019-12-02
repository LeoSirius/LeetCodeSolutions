#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m, n;
        m = matrix.size();
        if (m) n = matrix[0].size();
        
        bool is_first_row_zero = false, is_first_col_zero = false;

        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                is_first_col_zero = true;
                break;
            }
        }
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                is_first_row_zero = true;
                break;
            }
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = matrix[0][j] = 0;
                }
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
        }
        if (is_first_row_zero) {
            for (int j = 0; j < n; j++)
                matrix[0][j] = 0;
        }
        if (is_first_col_zero) {
            for (int i = 0; i < m; i++)
                matrix[i][0] = 0;
        }
    }
};

void test(string test_name, vector<vector<int>> &matrix, vector<vector<int>> expected)
{
    Solution s;
    s.setZeroes(matrix);
    if (matrix == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<int>> matrix1 = {
        {1,1,1},
        {1,0,1},
        {1,1,1}
    };
    vector<vector<int>> expected1 = {
        {1,0,1},
        {0,0,0},
        {1,0,1}
    };
    test("test1", matrix1, expected1);

    vector<vector<int>> matrix2 = {
        {0,1,2,0},
        {3,4,5,2},
        {1,3,1,5},
    };
    vector<vector<int>> expected2 = {
        {0,0,0,0},
        {0,4,5,0},
        {0,3,1,0}
    };
    test("test2", matrix2, expected2);

    vector<vector<int>> matrix3 = {
        {1},
        {0}
    };
    vector<vector<int>> expected3 = {
        {0},
        {0}
    };
    test("test3", matrix3, expected3);

    return 0;
}