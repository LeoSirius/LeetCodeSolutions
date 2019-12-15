#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        if (matrix.size() == 0) return res;
        int rbegin, rend, cbegin, cend;
        rbegin = cbegin = 0;
        rend = matrix.size() - 1;
        cend = matrix[0].size() - 1;

        while (rbegin <= rend && cbegin <= cend) {
            for (int i = cbegin; i <= cend; i++) {
                res.push_back(matrix[rbegin][i]);
            }
            rbegin++;
            for (int i = rbegin; i <= rend; i++) {
                res.push_back(matrix[i][cend]);
            }
            cend--;
            if (rbegin <= rend) {
                for (int i = cend; i >= cbegin; i--) {
                    res.push_back(matrix[rend][i]);
                }
            }
            rend--;
            if (cbegin <= cend) {
                for (int i = rend; i >= rbegin; i--) {
                    res.push_back(matrix[i][cbegin]);
                }
            }
            cbegin++;
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