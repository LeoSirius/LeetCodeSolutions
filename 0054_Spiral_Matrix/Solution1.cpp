#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        if (matrix.size() < 1) return res;
        int row_begin, row_end, col_begin, col_end;
        row_begin = col_begin = 0;
        row_end = matrix.size() - 1;
        col_end = matrix[0].size() - 1;

        while (row_begin <= row_end && col_begin <= col_end) {
            for (int i = col_begin; i <= col_end; i++) {
                res.push_back(matrix[row_begin][i]);
            }
            row_begin++;
            for (int i = row_begin; i <= row_end; i++) {
                res.push_back(matrix[i][col_end]);
            }
            col_end--;
            if (row_begin <= row_end) {
                // row_begin <= row_end， 说明还有行，因此可以left扫描
                // 这里需要检查，是因为while中的条件是等于，而在第一个for之后，row_begin++
                for (int i = col_end; i >= col_begin; i--) {
                    res.push_back(matrix[row_end][i]);
                }
            }
            row_end--;
            if (col_begin <= col_end) {
                // col_begin <= col_end， 说明还有列，因此可以up扫描
                for (int i = row_end; i >= row_begin; i--) {
                    res.push_back(matrix[i][col_begin]);
                }
            }
            col_begin++;
        }
        return res;
    }
};

void test(string test_name, vector<vector<int>> &matrix, vector<int> &expected)
{
    Solution s;
    if (s.spiralOrder(matrix) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<int>> matrix1 = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };
    vector<int> expected1 = {1,2,3,6,9,8,7,4,5};
    test("test1", matrix1, expected1);

    vector<vector<int>> matrix2 = {};
    vector<int> expected2 = {};
    test("test2", matrix2, expected2);

    vector<vector<int>> matrix3 = {
        {1,2,3,4},
        {5,6,7,8},
        {9,10,11,12}
    };
    vector<int> expected3 = {1,2,3,4,8,12,11,10,9,5,6,7};
    test("test3", matrix3, expected3);

    return 0;
}