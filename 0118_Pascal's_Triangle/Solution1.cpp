#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if (numRows == 0) return {};
        else if (numRows == 1) return {{1}};
        else if (numRows == 2) return {{1},{1,1}};
        vector<vector<int>> res {{1}, {1,1}};
        for (int n = 2; n < numRows; n++) {
            vector<int> row = {1};
            for (int i = 1; i < n; i++) {
                row.push_back(res[n-1][i] + res[n-1][i-1]);
            }
            row.push_back(1);
            res.push_back(row);
        }
        return res;
    }
};

void test(string test_name, int n, vector<vector<int>> expected)
{
    Solution s;
    if (s.generate(n) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    // Input: 5
    // Output:
    // [
    //      [1],
    //     [1,1],
    //    [1,2,1],
    //   [1,3,3,1],
    //  [1,4,6,4,1]
    // ]
    int n1 = 5;
    vector<vector<int>> expected1 = {
        {1},{1,1},{1,2,1},{1,3,3,1},{1,4,6,4,1}
    };
    test("test1", n1, expected1);

    return 0;
}
