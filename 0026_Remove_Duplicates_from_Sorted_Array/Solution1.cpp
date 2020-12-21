#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int new_tail = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[new_tail] != nums[i]) {
                nums[++new_tail] = nums[i];
            }
        }
        return new_tail + 1;
    }
};

void test(string test_name, vector<int> &nums, vector<int> &expected)
{
    Solution s;
    int len = s.removeDuplicates(nums);
    if (vector<int> (nums.begin(), nums.begin() + len) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {1, 1, 2};
    vector<int> expected1 = {1, 2};
    test("test1", nums1, expected1);

    vector<int> nums2 = {};
    vector<int> exptected2 = {};
    test("test2", nums2, exptected2);

    vector<int> nums3 = {1, 1};
    vector<int> expected3 = {1};
    test("test3", nums3, expected3);

    vector<int> nums4 = {0,0,1,1,1,2,2,3,3,4};
    vector<int> expected4 = {0,1,2,3,4};
    test("test4", nums4, expected4);

    return 0;
}
