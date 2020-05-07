#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        int mid;
        while (l < r) {
            mid = l + (r - l) / 2;
            if (nums[mid] < nums[mid+1])
                l = mid + 1;
            else
                r = mid;
        }
        return l;
    }
};

void test(string test_name, vector<int>& nums, vector<int> expected)
{
    int res = Solution().findPeakElement(nums);
    if (find(expected.begin(), expected.end(), res) != expected.end())
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {1,2,3,1};
    vector<int> expected1 = {2};
    test("test1", nums1, expected1);

    vector<int> nums2 = {1,2,1,3,5,6,4};
    vector<int> expected2 = {1, 5};
    test("test2", nums2, expected2);

    return 0;
}
