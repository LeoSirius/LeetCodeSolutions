
#include <iostream>
#include <vector>
using namespace std;

class Solution {
    vector<vector<int>> ans;

public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        perm(nums, 0, nums.size() - 1);
        return ans;
    }
    
    void perm(vector<int> nums, int left, int right) {
        if (left == right)
            ans.push_back(nums);
        else {
            for (int i = left; i <= right; i++) {
                if (i != left && nums[left] == nums[i]) continue;  // 去重
                swap(nums[left], nums[i]);
                perm(nums, left + 1, right);
            }
        }
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

