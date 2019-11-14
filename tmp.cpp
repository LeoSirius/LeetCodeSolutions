#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int len = nums.size();
        if (len == 0) return -1;

        int left, right, mid, small;
        
        left = 0, right = len - 1;
        while (left < right) {
            mid = left + (right - left) / 2;
            if (nums[mid] > nums[right])
                left = mid + 1;
            else
                right = mid;
        }

        small = left;
        left = 0;
        right = len - 1;
        if (nums[small] <= target && target <= nums[right])
            left = small;
        else
            right = small - 1;

        while (left <= right) {
            mid = left + (right - left) / 2;
            if (target > nums[mid])
                left = mid + 1;
            else if (target < nums[mid])
                right = mid - 1;
            else
                return mid;
        }
        return -1;
    }
};

void test(string test_name, vector<int>& nums, int target, int expected)
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
    vector<int> nums1 = {4,5,6,7,0,1,2};
    int target1 = 0;
    int expected1 = 4;
    test("test1", nums1, target1, expected1);
}
