#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (0 < i && nums[i] == nums[i-1])
                continue;
            for (int j = i + 1; j < nums.size(); j++) {
                if (i + 1 < j && nums[j] == nums[j-1])
                    continue;
                int l = j + 1;
                int r = nums.size() - 1;
                while (l < r) {
                    int sum = nums[i] + nums[j] + nums[l] + nums[r];
                    if (sum == target) {
                        res.push_back(vector<int>{nums[i], nums[j], nums[l], nums[r]});
                        while (l < r && nums[l+1] == nums[l]) l++;
                        while (l < r && nums[r-1] == nums[r]) r--;
                        l++; r--;
                    } else if (sum < target)
                        l++;
                    else
                        r--;
                }
            }
        }
        return res;
    }
};

void test(string test_name, vector<int> &nums, int target, vector<vector<int>> &expected)
{
    Solution s;
    vector<vector<int>> res = s.fourSum(nums, target);
    vector<vector<int>> exp = expected;
    for (int i = 0; i < res.size(); i++) {
        sort(res[i].begin(), res[i].end());
    }
    sort(res.begin(), res.end());
    for (int i = 0; i < exp.size(); i++) {
        sort(exp[i].begin(), exp[i].end());
    }
    sort(exp.begin(), exp.end());
    if (res == exp) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {1, 0, -1, 0, -2, 2};
    int target1 = 0;
    vector<vector<int>> expected1 = {
        {-1,  0, 0, 1},
        {-2, -1, 1, 2},
        {-2,  0, 0, 2}
    };
    test("test1", nums1, target1, expected1);

    vector<int> nums2 = {-3,-2,-1,0,0,1,2,3};
    int target2 = 0;
    vector<vector<int>> expected2 = {
        {-3,-2,2,3},
        {-3,-1,1,3},
        {-3,0,0,3},
        {-3,0,1,2},
        {-2,-1,0,3},
        {-2,-1,1,2},
        {-2,0,0,2},
        {-1,0,0,1}
    };
    test("test2", nums2, target2, expected2);

    vector<int> nums3 = {0,0,0,0};
    int target3 = 0;
    vector<vector<int>> expected3 = {{0,0,0,0}};
    test("test3", nums3, target3, expected3);

    return 0;
}