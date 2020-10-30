#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res = {-1, -1};
        unordered_map<int, int> mp;    // val to idx
        for (int i = 0; i < nums.size(); i++) {
            int num2find = target - nums[i];
            res[0] = i;
            if (mp.find(num2find) != mp.end()) {
                res[1] = mp[num2find];
                return res;
            }
            mp[nums[i]] = i;
        }
        return res;
    }
};

void test(string test_name, vector<int> &nums, int target, vector<int> expected)
{
    vector<int> res = Solution().twoSum(nums, target);
    sort(res.begin(), res.end());
    sort(expected.begin(), expected.end());
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}


int main()
{
    vector<int> nums1 = {2, 7, 11, 15};
    int target1 = 9;
    vector<int> expected1 = {0, 1};
    test("test1", nums1, target1, expected1);
    return 0;
}

// Given an array of integers, return indices of the two numbers 
// such that they add up to a specific target.

// You may assume that each input would have exactly one solution,
//  and you may not use the same element twice.

