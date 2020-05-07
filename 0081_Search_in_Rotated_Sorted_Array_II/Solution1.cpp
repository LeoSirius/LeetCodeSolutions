#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        int mid;
        while (l <= r) {
            while (l < r && nums[l] == nums[l+1]) l++;
            while (l < r && nums[r] == nums[r-1]) r--;
            mid = l + (r - l) / 2;
            if (nums[mid] == target)
                return true;
            if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target < nums[mid])   // 必须有nums[l] <= target
                    r = mid - 1;
                else
                    l = mid + 1;
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
    bool res = Solution().search(nums, target);
    if (res == expected) {
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

    vector<int> nums4 = {1};
    int target4 = 0;
    bool expected4 = false;
    test("test4", nums4, target4, expected4);

    vector<int> nums5 = {3,1};
    int target5 = 1;
    bool expected5 = true;
    test("test5", nums5, target5, expected5);

    vector<int> nums6 = {5, 1, 3};
    int target6 = 3;
    bool expected6 = true;
    test("test6", nums6, target6, expected6);

    vector<int> nums7 = {1,3,1,1,1};
    int target7 = 3;
    bool expected7 = true;
    test("test7", nums7, target7, expected7);

    return 0;
}
