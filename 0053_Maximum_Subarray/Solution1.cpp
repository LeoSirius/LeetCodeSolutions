#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res = nums[0];
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            res = max(sum, res);
            sum = max(sum, 0);
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