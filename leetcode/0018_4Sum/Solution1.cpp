#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        if (nums.size() < 4) return res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 3; i++) {
            if (i > 0 && nums[i-1] == nums[i]) continue;
            for (int j = i + 1; j < nums.size() - 2; j++) {
                if (j > i + 1 && nums[j-1] == nums[j]) continue;
                int left = j + 1, right = nums.size() - 1;
                while (left < right) {
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum == target) {
                        res.push_back(vector<int>{nums[i], nums[j], nums[left], nums[right]});
                        while (left < right && nums[left+1] == nums[left]) left++;
                        while (left < right && nums[right-1] == nums[right]) right--;
                        left++; right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
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
    return 0;
}