#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int reach = 0, i = 0;
        for (; i < nums.size() && i <= reach; ++i)
            reach = max(reach, i + nums[i]);
        return i == nums.size();
    }
};

void test(string test_name, vector<int> &nums, bool expected)
{
    bool res = Solution().canJump(nums);
    if (res == expected) {
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

    vector<int> nums3 = {0};
    bool expected3 = true;
    test("test3", nums3, expected3);

    return 0;
}

