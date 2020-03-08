#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            while (nums[i] >= 1 && nums[i] <= n && nums[nums[i]-1] != nums[i])
                swap(nums[nums[i]-1], nums[i]);
        }
        // 上面那个循环后、前三个例子的nums分别是：  可以看到在1-nums.size()之外的数是不会受影响的
        // 1 2 0
        // 1 -1 3 4
        // 7 8 9 11 12
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        return n + 1;
    }
};

void test(string test_name, vector<int> &nums, int expected)
{
    int res = Solution().firstMissingPositive(nums);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {1,2,0};
    int expected1 = 3;
    test("test1", nums1, expected1);

    vector<int> nums2 = {3,4,-1,1};
    int expected2 = 2;
    test("test2", nums2, expected2);

    vector<int> nums3 = {7,8,9,11,12};
    int expected3 = 1;
    test("test3", nums3, expected3);

    return 0;
}
