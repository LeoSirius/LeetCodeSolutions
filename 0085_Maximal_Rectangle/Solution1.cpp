#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int m = matrix.size();
        int n = m ? matrix[0].size() : 0;
        if (!n)
            return 0;

        // 注意[left, right)是左闭右开的
        int left[n], right[n], height[n];
        fill_n(left, n, 0);
        fill_n(right, n, n);
        fill_n(height, n, 0);
        int max_area;

        for (int i = 0; i < m; ++i) {
            int cur_left = 0, cur_right = n;
            for (int j = 0; j < n; ++j) {
                if(matrix[i][j] == '1')
                    ++height[j];
                else
                    height[j] = 0;
            }

            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == '1')
                    left[j] = max(left[j], cur_left);
                else {
                    left[j] = 0;
                    cur_left = j + 1;
                }
            }

            for (int j = n-1; j >= 0; --j) {
                if (matrix[i][j] == '1')
                    right[j] = min(right[j], cur_right);
                else {
                    right[j] = n;
                    cur_right = j;
                }
            }

            for (int j = 0; j < n; ++j) {
                max_area = max(max_area, (right[j] - left[j]) * height[j]);
            }
        }
        return max_area;
    }
};

void test(string test_name, vector<vector<char>>& matrix, int expected)
{
    int res = Solution().maximalRectangle(matrix);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{

    vector<vector<char>> matrix1 = {
        {'1','0','1','0','0'},
        {'1','0','1','1','1'},
        {'1','1','1','1','1'},
        {'1','0','0','1','0'}
    };
    int expected1 = 6;
    test("test1", matrix1, expected1);

    return 0;
}

