#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); i++) {
            if (mp.count(nums[i]) == 0) {
                mp[nums[i]] = i;
            } else if (i - mp[nums[i]] <= k) {
                return true;
            } else {
                mp[nums[i]] = i;
            }
        }
        return false;
    }
};

void test(string test_name, vector<int> nums, int k, bool expected)
{
    bool res = Solution().containsNearbyDuplicate(nums, k);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {1,2,3,1};
    int k1 = 3;
    bool expected1 = true;
    test("test1", nums1, k1, expected1);

    vector<int> nums2 = {1,0,1,1};
    int k2 = 1;
    bool expected2 = true;
    test("test2", nums2, k2, expected2);

    vector<int> nums3 = {1,2,3,1,2,3};
    int k3 = 2;
    bool expected3 = false;
    test("test3", nums3, k3, expected3);

    return 0;
}
