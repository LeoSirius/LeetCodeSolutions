#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        int i = 0;
        while (i < nums.size()) {
            if (nums[i] == 0 && i > left) {
                swap(nums[left++], nums[i]);
            } else if (nums[i] == 2 && i < right) {
                swap(nums[right--], nums[i]);
            } else {
                i++;
            }
        }
    }
};

void test(string test_name, vector<int> &nums, vector<int> &expected)
{
    Solution s;
    s.sortColors(nums);
    if (nums == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {2,0,2,1,1,0};
    vector<int> expected1 = {0,0,1,1,2,2};
    test("test1", nums1, expected1);
    return 0;
}
