#include <iostream>
#include <vector>
using namespace std;

class Solution {
    bool is_odd(int n)
    {
        return n % 2 == 1;
    }
public:
    vector<int> exchange(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            while (l < r && is_odd(nums[l])) l++;
            while (l < r && !is_odd(nums[r])) r--;
            swap(nums[l++], nums[r--]);
        }
        return nums;
    }
};

void test(string test_name, vector<int>& nums, vector<vector<int>> expected)
{
    vector<int> res = Solution().exchange(nums);
    bool success = false;
    for (auto item : expected) {
        if (item == res) {
            success = true;
            break;
        }
    }
    if (success)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {1,2,3,4};
    vector<vector<int>> expected1 = {
        {1,3,2,4},
        {3,1,2,4}
    };
    test("test1", nums1, expected1);

    return 0;
}



// 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，
// 所有偶数位于数组的后半部分。

//  

// 示例：

// 输入：nums = [1,2,3,4]
// 输出：[1,3,2,4] 
// 注：[3,1,2,4] 也是正确的答案之一。
//  

// 提示：

// 1 <= nums.length <= 50000
// 1 <= nums[i] <= 10000

