#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int i = 0;
        for (int reach = 0; i < nums.size() && i <= reach; i++) {
            reach = max(i + nums[i], reach);
        }
        return i == nums.size();
    }
};

void test(string test_name, vector<int> &nums, bool expected)
{
    Solution s;
    if (s.canJump(nums) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {2,3,1,1,4};
    bool expected1 = true;
    test("test1", nums1, expected1);

    vector<int> nums2 = {3,2,1,0,4};
    bool expected2 = false;
    test("test2", nums2, expected2);

    return 0;

}
