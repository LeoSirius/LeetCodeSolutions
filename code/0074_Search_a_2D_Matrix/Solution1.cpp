#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if (!m)
            return false;
        int n = matrix[0].size();

        int x = 0, y = n - 1;
        while (x < m && 0 <= y) {
            if (matrix[x][y] == target)
                return true;
            else if (matrix[x][y] < target)
                x++;
            else
                y--;
        }
        return false;
    }
};


void test(string test_name, vector<vector<int>> &matrix, int target, bool expected)
{
    Solution s;
    if (s.searchMatrix(matrix, target) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<int>> matrix1 = {
        {1,3,5,7},
        {10,11,16,20},
        {23,30,34,50}
    };
    int target1 = 3;
    bool expected1 = true;
    test("test1", matrix1, target1, expected1);

    vector<vector<int>> matrix2 = matrix1;
    int target2 = 13;
    bool expected2 = false;
    test("test2", matrix2, target2, expected2);

    vector<vector<int>> matrix3 = {{1}};
    int target3 = 2;
    bool expected3 = false;
    test("test3", matrix3, target3, expected3);

    vector<vector<int>> matrix4 = {{1}};
    int target4 = 1;
    bool expected4 = true;
    test("test4", matrix4, target4, expected4);

    return 0;
}

// Write an efficient algorithm that searches for a value in an m x n matrix.
//  This matrix has the following properties:

// Integers in each row are sorted from left to right.
// The first integer of each row is greater than the last integer of the previous row.

