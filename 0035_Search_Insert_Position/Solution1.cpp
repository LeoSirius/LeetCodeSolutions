#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size() == 0) return -1;
        int left = 0, right = nums.size() - 1;
        int mid;
        while(left <= right){
            mid = left + (right - left) / 2;
            if(nums[mid] == target) return mid;
            else if(target > nums[mid]) left = mid + 1;
            else right = mid - 1;
        }
        return left;
    }
};

void test(string test_name, vector<int> &nums, int target, int expected)
{
    Solution s;
    if (s.searchInsert(nums, target) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }

}

int main()
{
    vector<int> nums1 = {1, 3, 5, 6};
    int target1 = 2;
    int expected1 = 1;
    test("test1", nums1, target1, expected1);

    return 0;
}