#include<iostream>
#include<vector>
#include<unordered_map>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        unordered_map<int, int> my_map;
        for (int i = 0; i < nums.size(); i++) {
            int num_to_find = target - nums[i];
            if (my_map.find(num_to_find) != my_map.end()) {
                res = {i, my_map[num_to_find]};
                break;
            } else {
                my_map[nums[i]] = i;
            }
        }
        return res;
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