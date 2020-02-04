#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.size() == 0) return 0;
        int m = matrix.size();
        int n = matrix[0].size();
        int sz = 0;
        vector<int> pre(n, 0), cur(n, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!i || !j || matrix[i][j] == '0')
                    cur[j] = matrix[i][j] - '0';
                else
                    cur[j] = min(pre[j], min(pre[j-1], cur[j-1])) + 1;
                sz = max(sz, cur[j]);
            }
            pre = cur;
            fill(cur.begin(), cur.end(), 0);
        }
        return sz * sz;
    }
};

void test(string test_name, vector<vector<char>> &matrix, int expected)
{
    if (Solution().maximalSquare(matrix) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<char>> matrix1 = {
        {'1', '0', '1', '0', '0'},
        {'1', '0', '1', '1', '1'},
        {'1', '1', '1', '1', '1'},
        {'1', '0', '0', '1', '0'},
    };
    int expected1 = 4;
    test("test1", matrix1, expected1);

    return 0;
}
