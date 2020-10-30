#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int res, count = 0;
        for (int item : nums) {
            if (count == 0) {
                res = item;
                count++;
            } else {
                res == item ? count++ : count--;
            }
        }
        return res;
    }
};

void test(string test_name, vector<int>& nums, int expected)
{
    int res = Solution().majorityElement(nums);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {1, 2, 3, 2, 2, 2, 5, 4, 2};
    int expected1 = 2;
    test("test1", nums1, expected1);

    return 0;
}

// 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
// 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
//  

// 示例 1:

// 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
// 输出: 2
//  

// 限制：
// 1 <= 数组长度 <= 50000
