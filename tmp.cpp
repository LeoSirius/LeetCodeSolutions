#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int max_idx;
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (i == 0) {
                reverse(nums.begin(), nums.end());
                return;
            }
            if (nums[i-1] < nums[i]) {
                max_idx = i;
                break;
            }
        }
        for (int i = nums.size() - 1; i >= max_idx; i--) {
            if (nums[i] > nums[max_idx-1]) {
                swap(nums[i], nums[max_idx-1]);
                break;
            }
        }
        reverse(nums.begin() + max_idx, nums.end());
    }
};

void test(string test_name, vector<int> &nums, vector<int> &expected)
{
    Solution s;
    s.nextPermutation(nums);
    if (nums == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {1,2,3};
    vector<int> expected1 = {1,3,2};
    test("test1", nums1, expected1);

    vector<int> nums2 = {3,2,1};
    vector<int> expected2 = {1,2,3};
    test("test2", nums2, expected2);

    vector<int> nums3 = {1,1,5};
    vector<int> expected3 = {1,5,1};
    test("test3", nums3, expected3);

    vector<int> nums4 = {1,3,2};
    vector<int> expected4 = {2,1,3};
    test("test4", nums4, expected4);

    return 0;
}
