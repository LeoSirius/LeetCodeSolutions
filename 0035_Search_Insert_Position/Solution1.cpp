#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size() == 0)
            return 0;
        int l = 0, r = nums.size() - 1;
        int mid;
        while (l <= r) {
            mid = l + (r - l) / 2;
            if (nums[mid] == target)
                return mid;
            else if (target < nums[mid])
                r = mid - 1;
            else
                l = mid + 1;
        }
        return l;
    }
};

void test(string test_name, vector<int> &nums, int target, int expected)
{
    int res = Solution().searchInsert(nums, target);
    if (res == expected) {
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

    vector<int> nums2 = {1,3,5,6};
    int target2 = 7;
    int expected2 = 4;
    test("test2", nums2, target2, expected2);

    return 0;
}