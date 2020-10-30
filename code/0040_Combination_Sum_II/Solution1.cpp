#include <iostream>
#include <vector>
using namespace std;

class Solution {
    void dfs(vector<int>& candidates, int start, vector<int>& path, int target)
    {
        if (target == 0) {
            res.push_back(path);
            return;
        }
        for (int i = start; i < candidates.size() && candidates[i] <= target; i++) {
            if (start < i && candidates[i] == candidates[i-1]) continue;
            path.push_back(candidates[i]);
            dfs(candidates, i + 1, path, target - path.back());
            path.pop_back();
        }
    }
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        dfs(candidates, 0, path, target);
        return res;
    }
};


void test(string test_name, vector<int> &candidates, int target, vector<vector<int>> &expected)
{
    Solution s;
    vector<vector<int>> res;
    res = s.combinationSum2(candidates, target);
    for (int i = 0; i < res.size(); i++) {
        sort(res[i].begin(), res[i].end());
    }
    sort(res.begin(), res.end());
    for (int i = 0; i < expected.size(); i++) {
        sort(expected[i].begin(), expected[i].end());
    }
    sort(expected.begin(), expected.end());
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " faield." << endl;
    }
}

int main()
{
    vector<int> candidates1 = {10, 1, 2, 7, 6, 1, 5};
    int target1 = 8;
    vector<vector<int>> expected1 = {
        {1, 1, 6},
        {1, 2, 5},
        {1, 7},
        {2, 6}
    };
    test("test1", candidates1, target1, expected1);
    return 0;
}
