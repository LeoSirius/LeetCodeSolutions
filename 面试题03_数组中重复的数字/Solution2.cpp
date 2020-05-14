#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); i++) {
            if (mp.find(nums[i]) != mp.end())
                return nums[i];
            mp[nums[i]]++;
        }
        return -1;
    }
};

void test(string test_name, vector<int> nums, vector<int> expected)
{
    int res = Solution().findRepeatNumber(nums);
    if (find(expected.begin(), expected.end(), res) != expected.end())
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {2, 3, 1, 0, 2, 5, 3};
    vector<int> expected1 = {2,3};
    test("test1", nums1, expected1);

    return 0;
}

// [2, 3, 1, 0, 2, 5, 3]
// 输出：2 或 3 

// 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
// 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
// 请找出数组中任意一个重复的数字。

// 限制：

// 2 <= n <= 100000
