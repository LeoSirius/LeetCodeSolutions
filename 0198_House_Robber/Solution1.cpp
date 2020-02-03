#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];
        vector<int> dp(nums.size(), 0);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size(); i++) {
            dp[i] = max(dp[i-2] + nums[i], dp[i-1]);
        }
        return dp[dp.size()-1];
    }
};

void test(string test_name, vector<int> &nums, int expected)
{
    if (Solution().rob(nums) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}



int main()
{
    vector<int> nums1 = {1,2,3,1};
    int expected1 = 4;
    test("test1", nums1, expected1);

    vector<int> nums2 = {2,7,9,3,1};
    int expected2 = 12;
    test("test2", nums2, expected2);


    vector<int> nums3 = {};
    int expected3 = 0;
    test("test3", nums3, expected3);

    return 0;
}