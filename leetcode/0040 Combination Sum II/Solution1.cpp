#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
    void dfs(vector<int> &candidates, int target, int begin, vector<int> &path, vector<vector<int>> &res)
    {
        if (target <= 0) {
            res.push_back(path);
            return;
        }
        for (int i = begin; i < candidates.size() && candidates[i] <= target; i++) {
            if (i > begin && candidates[i-1] == candidates[i]) continue;
            path.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], i + 1, path, res);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;
        sort(candidates.begin(), candidates.end());
        dfs(candidates, target, 0, path, res);
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