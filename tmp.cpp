#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        
    }
};

void test(string test_name, vector<int> &nums, int expected)
{
    if (Solution().rob(nums) == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {1,2,3,1};
    int expected1 = 4;
    test("test1", nums1, expected1);

    vector<int> nums2 = {2,7,9,3,1};
    int expected2 = 12;
    test("test2", nums2, expected2);

    return 0;
}

//dp 方程 dp[i] = max(dp[i-2]+nums[i], dp[i-1])

