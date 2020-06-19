#include <iostream>
#include <vector>
using namespace std;

class Solution {
    void dfs(vector<vector<int>>& res, vector<int>& nums, int start, int size)
    {
        if (start == size) {
            res.push_back(nums);
            return;
        }

        for (int i = start; i < size; i++) {
            swap(nums[start], nums[i]);
            dfs(res, nums, start + 1, size);   // 注意这里是start + 1
            swap(nums[start], nums[i]);
        }
    }

public:
    
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        dfs(res, nums, 0, nums.size());
        return res;
    }
};

void test(string test_name, vector<int> nums, vector<vector<int>> expected)
{
    vector<vector<int>> res = Solution().permute(nums);
    sort(expected.begin(), expected.end());
    sort(res.begin(), res.end());
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {1,2,3};
    vector<vector<int>> expected1 = {
        {1,2,3},
        {1,3,2},
        {2,1,3},
        {2,3,1},
        {3,2,1},
        {3,1,2},
    };
    test("test1", nums1, expected1);

    return 0;
}

// Given a collection of distinct integers, return all possible permutations.

// Example:

// Input: [1,2,3]
// Output:
// [
//   [1,2,3],
//   [1,3,2],
//   [2,1,3],
//   [2,3,1],
//   [3,1,2],
//   [3,2,1]
// ]
