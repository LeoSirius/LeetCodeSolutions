#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int new_tail = 0;
        for (int n : nums)
            if (new_tail < 2 || n > nums[new_tail-2]) {
                nums[new_tail++] = n;
            }
        return new_tail;
    }
};

void test(string test_name, vector<int> &nums, int expected)
{
    Solution s;
    if (s.removeDuplicates(nums) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {1,1,1,2,2,3};
    int expected1 = 5;
    test("test1", nums1, expected1);

    vector<int> nums2 = {0,0,1,1,1,1,2,3,3};
    int expected2 = 7;
    test("test2", nums2, expected2);

    return 0;
}
