
#include <iostream>
#include <vector>
using namespace std;

class Solution {
    void dfs(vector<int> nums, int left, int right)
    {
        if (left == right) {
            res.push_back(nums);
            return;
        }
        for (int i = left; i <= right; i++) {
            if (left < i && nums[left] == nums[i]) continue;
            swap(nums[left], nums[i]);
            dfs(nums, left + 1, right);    // 注意dfs的第一个参数不是引用，所以调用之后没有swap back
        }
    }
public:
    vector<vector<int>> res;
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        dfs(nums, 0, nums.size() - 1);
        return res;
    }
};

void test(string test_name, vector<int> &nums, vector<vector<int>> expected)
{
    vector<vector<int>> res = Solution().permuteUnique(nums);
    sort(res.begin(), res.end());
    sort(expected.begin(), expected.end());
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {1,1,2};
    vector<vector<int>> expected1 = {
        {1,1,2},
        {1,2,1},
        {2,1,1},
    };
    test("test1", nums1, expected1);

    vector<int> nums2 = {3,3,0,3};
    vector<vector<int>> expected2 = {
        {0,3,3,3},
        {3,0,3,3},
        {3,3,0,3},
        {3,3,3,0}
    };
    test("test2", nums2, expected2);

    return 0;
}

// Given a collection of numbers that might contain duplicates, 
// return all possible unique permutations.

// Example:

// Input: [1,1,2]
// Output:
// [
//   [1,1,2],
//   [1,2,1],
//   [2,1,1]
// ]

