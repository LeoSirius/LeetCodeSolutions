#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        reverse(matrix.begin(), matrix.end());
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = i + 1; j < matrix.size(); j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};

void test(string test_name, vector<vector<int>> matrix, vector<vector<int>> &expected)
{
    Solution s;
    s.rotate(matrix);
    if (matrix == expected) {
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
        {7,8,9},
    };
    vector<vector<int>> expected1 = {
        {7,4,1},
        {8,5,2},
        {9,6,3},
    };
    test("test1", matrix1, expected1);
    return 0;
}

