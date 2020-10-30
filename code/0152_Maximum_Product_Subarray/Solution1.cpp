#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        int imax = res, imin = res;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) swap(imax, imin);
            imax = max(nums[i], nums[i] * imax);
            imin = min(nums[i], nums[i] * imin);
            res = max(res, imax);
        }
        return res;
    }
};

void test(string test_name, vector<int> nums, int expected)
{
    Solution s;
    if (s.maxProduct(nums) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {2,3,-2,4};
    int expected1 = 6;
    test("test1", nums1, expected1);

    vector<int> nums2 = {-2,0,-1};
    int expected2 = 0;
    test("test2", nums2, expected2);

    return 0;
}

// Example 1:

// Input: [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.
// Example 2:

// Input: [-2,0,-1]
// Output: 0
// Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
