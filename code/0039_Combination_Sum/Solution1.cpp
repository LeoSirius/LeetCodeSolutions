#include <iostream>
#include <vector>
using namespace std;

class Solution {
    vector<vector<int>> res;
    void dfs(int sum, int start, vector<int>& candidates, vector<int> path)
    {
        if (sum < 0) return;
        if (sum == 0) {
            res.push_back(path);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            path.push_back(candidates[i]);
            dfs(sum - candidates[i], i, candidates, path);
            path.pop_back();
        }
    }

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        dfs(target, 0, candidates, path);
        return res;
    }
};


void test(string test_name, vector<int> &candidates, int target, vector<vector<int>> &expected)
{
    Solution s;
    vector<vector<int>> res = s.combinationSum(candidates, target);
    for (auto item : res) {
        sort(item.begin(), item.end());
    }
    sort(res.begin(), res.end());
    for (auto item : expected) {
        sort(item.begin(), item.end());
    }
    sort(expected.begin(), expected.end());
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }

}

int main()
{
    vector<int> candidates1 = {2,3,6,7};
    int target1 = 7;
    vector<vector<int>> expected1 = {
        {7},{2,2,3}
    };
    test("test1", candidates1, target1, expected1);

    vector<int> candidates2 = {2,3,5};
    int target2 = 8;
    vector<vector<int>> expected2 = {
        {2,2,2,2},{2,3,3},{3,5}
    };
    test("test2", candidates2, target2, expected2);

    return 0;
}