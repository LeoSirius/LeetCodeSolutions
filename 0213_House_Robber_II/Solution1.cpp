#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];
        vector<int> dp(nums.size(), 0);   // start from first house
        dp[0] = dp[1] = nums[0];
        vector<int> dp2(nums.size(), 0);  // start from second house
        dp2[1] = nums[1];
        for (int i = 2; i < nums.size(); i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i]);
        }
        return max(dp[dp.size()-2], dp2[dp2.size()-1]);
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
    vector<int> nums1 = {2,3,2};
    int expected1 = 3;
    test("test1", nums1, expected1);

    vector<int> nums2 = {1,2,3,1};
    int expected2 = 4;
    test("test2", nums2, expected2);

    vector<int> nums3 = {4,1,2,7,5,3,1};
    int expected3 = 14;
    test("test3", nums3, expected3);

    return 0;
}