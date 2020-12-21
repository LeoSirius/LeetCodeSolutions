#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        for (int i = triangle.size() - 2; i >= 0; i--)
            for (int j = 0; j < triangle[i].size(); j++)
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]);
        return triangle[0][0];
    }
};

void test(string test_name, vector<vector<int>>& triangle, int expected)
{
    Solution s;
    if (s.minimumTotal(triangle) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    // [
    //      [2],
    //     [3,4],
    //    [6,5,7],
    //   [4,1,8,3]
    // ]
    // The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
    vector<vector<int>> triangle1 = {
        {2},{3,4},{6,5,7},{4,1,8,3}
    };
    int expected1 = 11;
    test("test1", triangle1, expected1);

    return 0;
}
