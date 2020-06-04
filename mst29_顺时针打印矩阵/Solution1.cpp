#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        if (matrix.empty()) return res;

        int rbegin = 0, rend = matrix.size() - 1;
        int cbegin = 0, cend = matrix[0].size() - 1;

        while (true) {
            for (int i = cbegin; i <= cend; i++) res.push_back(matrix[rbegin][i]);
            if (++rbegin > rend) break;

            for (int i = rbegin; i <= rend; i++) res.push_back(matrix[i][cend]);
            if (--cend < cbegin) break;

            for (int i = cend; cbegin <= i; i--) res.push_back(matrix[rend][i]);
            if (--rend < rbegin) break;

            for (int i = rend; rbegin <= i; i--) res.push_back(matrix[i][cbegin]);
            if (++cbegin > cend) break;
        }
        return res;
    }
};

void test(string test_name, vector<vector<int>>& matrix, vector<int> expected)
{
    vector<int> res = Solution().spiralOrder(matrix);
    if (res == expected)
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
    vector<int> expected1 = {1,2,3,6,9,8,7,4,5};
    test("test1", matrix1, expected1);

    vector<vector<int>> matrix2 = {
        {1,2,3,4},
        {5,6,7,8},
        {9,10,11,12}
    };
    vector<int> expected2 = {1,2,3,4,8,12,11,10,9,5,6,7};
    test("test2", matrix2, expected2);

    return 0;
}

// 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

// 限制：

// 0 <= matrix.length <= 100
// 0 <= matrix[i].length <= 100
