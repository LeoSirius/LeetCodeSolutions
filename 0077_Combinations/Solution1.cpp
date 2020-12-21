#include <iostream>
#include <vector>
using namespace std;

class Solution {
    void dfs(int n, int k, int start, vector<int> path)
    {
        if (path.size() == k) {
            res.push_back(path);
            return;
        }
        for (int i = start + 1; i <= n; i++) {
            path.push_back(i);
            dfs(n, k, i, path);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> res;
    vector<vector<int>> combine(int n, int k) {
        vector<int> path;
        dfs(n, k, 0, path);
        return res;
    }
};


void test(string test_name, int n, int k, vector<vector<int>> expected)
{
    vector<vector<int>> res = Solution().combine(n, k);
    sort(res.begin(), res.end());
    sort(expected.begin(), expected.end());
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int n1 = 4, k1 = 2;
    vector<vector<int>> expected1 = {
        {2,4,}, {3,4}, {2,3}, {1,2}, {1,3}, {1,4}
    };
    test("test1", n1, k1, expected1);

    return 0;
}

// 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

// 示例:

// 输入: n = 4, k = 2
// 输出:
// [
//   [2,4],
//   [3,4],
//   [2,3],
//   [1,2],
//   [1,3],
//   [1,4],
// ]

