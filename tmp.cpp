#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.size() < 3) return res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    res.push_back(vector<int> {nums[i], nums[left], nums[right]});
                    while (left < right && nums[left] == nums[left+1]) left++;
                    left++;
                    while (left < right && nums[right] == nums[right-1]) right--;
                    right--;
                } else if (sum > 0) {
                    right--;
                } else {
                    left++;
                }
            }
        }
        return res;
    }
};

void test(string test_name, vector<int> &nums, vector<vector<int>> &expected)
{
    Solution s;
    if (s.threeSum(nums) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> param1 = {-1, 0, 1, 2, -1, -1};
    vector<vector<int>> expected1 = {
        {-1, -1, 2},
        {-1, 0, 1},
    };
    test("test1", param1, expected1);

    vector<int> param2 = {};
    vector<vector<int>> expected2;
    test("test2", param2, expected2);

    vector<int> param3 = {0};
    vector<vector<int>> expected3;
    test("test3", param3, expected3);

    return 0;
}
