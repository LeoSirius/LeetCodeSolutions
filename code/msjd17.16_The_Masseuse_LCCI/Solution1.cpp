#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int massage(vector<int>& nums) {
        int len = nums.size();
        if (!len)
            return 0;
        else if (len == 1)
            return nums[0];
        else if (len == 2)
            return max(nums[0], nums[1]);

        vector<int> dp(len, 0);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        for (int i = 2; i < len; i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        return dp[len-1];
    }
};

void test(string test_name, vector<int>& nums, int expected)
{
    int res = Solution().massage(nums);
    if (res == expected) {
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

    vector<int> nums3 = {2,1,4,5,3,1,1,3};
    int expected3 = 12;
    test("test3", nums3, expected3);

    return 0;
}
