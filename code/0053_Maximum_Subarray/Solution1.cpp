#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp(nums.size());    //dp[i] means the maximum subarray ending with A[i];
        dp[0] = nums[0];
        int res = dp[0];
        for (int i = 1; i < nums.size(); i++) {
            dp[i] = max(0, dp[i-1]) + nums[i];
            res = max(res, dp[i]);
        }
        return res;
    }
};

void test(string test_name, vector<int> &nums, int expected)
{
    Solution s;
    if (s.maxSubArray(nums) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {-2,1,-3,4,-1,2,1,-5,4};
    int expected1 = 6;
    test("test1", nums1, expected1);
    return 0;
}
