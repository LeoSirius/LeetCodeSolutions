#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
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

    vector<int> nums2 = {1,3,5,6};
    int target2 = 7;
    int expected2 = 4;
    test("test2", nums2, target2, expected2);

    return 0;
}


// Given a sorted array and a target value, return the index if 
// the target is found. If not, return the index where it would be 
// if it were inserted in order.

// You may assume no duplicates in the array.

