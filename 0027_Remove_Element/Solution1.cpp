#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int tail = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[tail++] = nums[i];
            }
        }
        return tail;
    }
};

void test(string test_name, vector<int> &nums, int val, int expected)
{
    Solution s;
    if (s.removeElement(nums, val) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {3,2,2,3};
    int val1 = 3;
    int expected1 = 2;
    test("test1", nums1, val1, expected1);

    vector<int> nums2 = {0,1,2,2,3,0,4,2};
    int val2 = 2;
    int expected2 = 5;
    test("test2", nums2, val2, expected2);

    return 0;
}
