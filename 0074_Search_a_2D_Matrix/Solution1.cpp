#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0) return false;
        int m = 0, n = matrix[0].size() - 1;
        while (m < matrix.size() && n >= 0) {
            if (target == matrix[m][n]) {
                return true;
            } else if (target < matrix[m][n]) {
                n--;
            } else {
                m++;
            }
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

    return 0;
}
