#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); i++) {
            if (mp[nums[i]]++ >= 1) {
                return true;
            }
        }
        return false;
    }
};

void test(string test_name, vector<int> nums, bool expected)
{
    bool res = Solution().containsDuplicate(nums);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {1,2,3,1};
    bool expected1 = true;
    test("test1", nums1, expected1);

    vector<int> nums2 = {1,2,3,4};
    bool expected2 = false;
    test("test2", nums2, expected2);

    vector<int> nums3 = {1,1,1,3,3,4,3,2,4,2};
    bool expected3 = true;
    test("test3", nums3, expected3);

    return 0;
}
