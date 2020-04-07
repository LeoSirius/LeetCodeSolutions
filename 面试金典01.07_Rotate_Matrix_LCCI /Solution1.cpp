#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (matrix.empty())
            return;

        reverse(matrix.begin(), matrix.end());
        for (int i = 1; i < matrix.size(); ++i)
            for (int j = 0; j < i; ++j)
                swap(matrix[i][j], matrix[j][i]);
    }
};

void test(string test_name, vector<vector<int>>& matrix, vector<vector<int>>& expected)
{
    Solution().rotate(matrix);
    if (matrix == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<vector<int>> matrix1 = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };
    vector<vector<int>> expected1 = {
        {7,4,1},
        {8,5,2},
        {9,6,3}
    };
    test("test1", matrix1, expected1);

    vector<vector<int>> matrix2 = {
        { 5, 1, 9,11},
        { 2, 4, 8,10},
        {13, 3, 6, 7},
        {15,14,12,16}
    };
    vector<vector<int>> expected2 = {
        {15,13, 2, 5},
        {14, 3, 4, 1},
        {12, 6, 8, 9},
        {16, 7,10,11}
    };
    test("test2", matrix2, expected2);

    return 0;
}