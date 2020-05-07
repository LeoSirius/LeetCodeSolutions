#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        int mid;
        while (l < r) {
            mid = l + (r - l) / 2;
            // pivot即是最小点
            // 中间小于右边，则必然在mid的左边(或mid)，5 1 2 3 4     5 6 1 2 3 4
            // pivot <= mid，
            if (nums[mid] < nums[r])
                r = mid;
            else
                l = mid + 1;  // 中间大于等于右边，说明pivot越过了中间，则必然在右边。mid < pivot
        }
        return nums[l];       // 退出的时候l==r这里nums[l]和nums[r]是一样的
    }
};

void test(string test_name, vector<int>& nums, int expected)
{
    int res = Solution().findMin(nums);
    if (res == expected)
        cout << test_name + " success." << endl;
    else
        cout << test_name + " failed." << endl;
}

int main()
{
    vector<int> nums1 = {3,4,5,1,2};
    int expected1 = 1;
    test("test1", nums1, expected1);

    vector<int> nums2 = {4,5,6,7,0,1,2};
    int expected2 = 0;
    test("test2", nums2, expected2);

    return 0;
}
