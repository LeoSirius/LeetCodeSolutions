#include<iostream>
#include<vector>
#include<unordered_map>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        vector<int> cur_not_found;
        for (int i = 0; i < nums.size(); i++) {
            int num_to_find = target - nums[i];
        }
    }
};

void test(string test_name, vector<int> &nums, int target, vector<int> expected)
{
    Solution s;
    vector<int> a = s.twoSum(nums, target);
    vector<int> b = expected;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    if (a == b) {
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