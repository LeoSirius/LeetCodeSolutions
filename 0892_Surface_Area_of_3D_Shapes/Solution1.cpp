#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int surfaceArea(vector<vector<int>>& grid) {
        int res = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.size(); j++) {
                if (grid[i][j])
                    res += 4 * grid[i][j] + 2;
                if (i)
                    res -= min(grid[i-1][j], grid[i][j]) * 2;
                if (j)
                    res -= min(grid[i][j-1], grid[i][j]) * 2;
            }
        }
        return res;
    }
};

void test(string test_name, vector<vector<int>>& grid, int expected)
{
    int res = Solution().surfaceArea(grid);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<int>> grid1 = {{2}};
    int expected1 = 10;
    test("test1", grid1, expected1);

    vector<vector<int>> grid2 = {{1,2}, {3,4}};
    int expected2 = 34;
    test("test2", grid2, expected2);

    vector<vector<int>> grid3 = {{1,0}, {0, 2}};
    int expected3 = 16;
    test("test3", grid3, expected3);

    vector<vector<int>> grid4 = {{1,1,1},{1,0,1},{1,1,1}};
    int expected4 = 32;
    test("test4", grid4, expected4);

    vector<vector<int>> grid5 = {{2,2,2},{2,1,2},{2,2,2}};
    int expected5 = 46;
    test("test5", grid5, expected5);

    return 0;
}
