#include <iostream>
#include <vector>
using namespace std;

class Solution {
    void dfs(vector<int> path, int start, vector<int>& nums)
    {
        res.push_back(path);
        for (int i = start; i < nums.size(); i++) {
            path.push_back(nums[i]);
            dfs(path, i + 1, nums);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> res;
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> path;
        dfs(path, 0, nums);
        return res;
    }
};


void test(string test_name, vector<int> &nums, vector<vector<int>> &expected)
{
    vector<vector<int>> res = Solution().subsets(nums);
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
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {1,2,3};
    vector<vector<int>> expected1 = {
        {},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}
    };
    test("test1", nums1, expected1);

    return 0;
}

// Given a set of distinct integers, nums, return all possible subsets (the power set).

// Note: The solution set must not contain duplicate subsets.

// Example:

// Input: nums = [1,2,3]
// Output:
// [
//   [3],
//   [1],
//   [2],
//   [1,2,3],
//   [1,3],
//   [2,3],
//   [1,2],
//   []
// ]

