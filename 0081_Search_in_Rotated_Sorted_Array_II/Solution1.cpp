#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            while (l < r && nums[l] == nums[l+1]) l++;
            while (l < r && nums[r] == nums[r-1]) r--;
            int mid = l + (r-l) / 2;

            if (nums[mid] == target)
                return true;
            
            // 左半边有序 e.g. 4,5,6,7,0,1
            if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target < nums[mid])
                    r = mid - 1;  // e.g. target=5
                else
                    l = mid + 1;  // e.g. target=7
            } else {
                if (nums[mid] < target && target <= nums[r])
                    l = mid + 1;
                else
                    r = mid - 1;
            }
        }
        return false;
    }
};


void test(string test_name, vector<int> &nums, int target, bool expected)
{
    Solution s;
    if (s.search(nums, target) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {2,5,6,0,0,1,2};
    int target1 = 0;
    bool expected1 = true;
    test("test1", nums1, target1, expected1);

    vector<int> nums2 = {2,5,6,0,0,1,2};
    int target2 = 3;
    bool expected2 = false;
    test("test2", nums2, target2, expected2);

    vector<int> nums3 = {};
    int target3 = 5;
    bool expected3 = false;
    test("test3", nums3, target3, expected3);

    return 0;
}
