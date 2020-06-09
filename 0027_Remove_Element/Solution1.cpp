#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int new_tail = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val)
                nums[++new_tail] = nums[i];
        }
        return new_tail + 1;
    }
};


void test(string test_name, vector<int> &nums, int val, vector<int> expected)
{
    int len = Solution().removeElement(nums, val);
    if (vector<int>(nums.begin(), nums.begin() + len) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {3,2,2,3};
    int val1 = 3;
    vector<int> expected1 = {2,2};
    test("test1", nums1, val1, expected1);

    vector<int> nums2 = {0,1,2,2,3,0,4,2};
    int val2 = 2;
    vector<int> expected2 = {0,1,3,0,4};
    test("test2", nums2, val2, expected2);

    return 0;
}
