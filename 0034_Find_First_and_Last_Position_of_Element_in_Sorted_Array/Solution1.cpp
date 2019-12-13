#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res = {-1, -1};
        if (nums.size() == 0) return res;

        int left = 0, right = nums.size() - 1;
        int mid;
        while (left < right) {
            mid = left + (right - left) / 2;
            if (target > nums[mid]) left = mid + 1;
            else right = mid;
        }
        if (nums[left] != target) return res;       // target不在nums中
        else res[0] = left;

        right = nums.size() - 1;                    // left不用重置
        while (left < right) {
            mid = left + (right - left) / 2 + 1;    // +1 make mid biased to right
            if (target < nums[mid]) right = mid - 1;
            else left = mid;
        }
        res[1] = right;
        return res;
    }
};

void test(string test_name, vector<int> &nums, int target, vector<int> &expected)
{
    Solution s;
    if (s.searchRange(nums, target) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {5,7,7,8,8,10};
    int target1 = 8;
    vector<int> expected1 = {3,4};
    test("test1", nums1, target1, expected1);

    vector<int> nums2 = {5,7,7,8,8,10};
    int target2 = 6;
    vector<int> expected2 = {-1, -1};
    test("test2", nums2, target2, expected2);

    vector<int> nums3 = {};
    int target3 = 0;
    vector<int> expected3 = {-1, -1};
    test("test3", nums3, target3, expected3);

    vector<int> nums4 = {1};
    int target4 = 1;
    vector<int> expected4 = {0,0};
    test("test4", nums4, target4, expected4);

    return 0;
}
