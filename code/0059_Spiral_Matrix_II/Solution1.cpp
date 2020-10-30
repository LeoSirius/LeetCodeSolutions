#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n, vector<int>(n, 0));
        if (n < 1) return res;
        int num = 1;

        int row_begin, row_end, col_begin, col_end;

        row_begin = col_begin = 0;
        row_end = col_end = n - 1;

        while (row_begin <= row_end && col_begin <= col_end) {
            for (int i = col_begin; i <= col_end; i++) {
                res[row_begin][i] = num++;
            }
            row_begin++;

            for (int i = row_begin; i <= row_end; i++) {
                res[i][col_end] = num++;
            }
            col_end--;

            if (row_begin <= row_end) {
                for (int i = col_end; i >= col_begin; i--) {
                    res[row_end][i] = num++;
                }
            }
            row_end--;

            if (col_begin <= col_end) {
                for (int i = row_end; i >= row_begin; i--) {
                    res[i][col_begin] = num++;
                }
            }
            col_begin++;
        }
        return res;
    }
};

void test(string test_name, int n, vector<vector<int>> &expected)
{
    Solution s;
    if (s.generateMatrix(n) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 3;
    vector<vector<int>> expected1 = {
        {1,2,3},
        {8,9,4},
        {7,6,5},
    };
    test("test1", n1, expected1);

    return 0;
}
