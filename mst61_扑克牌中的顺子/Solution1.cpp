#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool isStraight(vector<int>& nums) {
        unordered_set<int> mset;
        int mi = 15, ma = -1;
        for (int n : nums) {
            if (n == 0) continue;
            if (mset.find(n) != mset.end()) return false;

            mi = min(mi, n);
            ma = max(ma, n);
            mset.insert(n);
        }
        return ma - mi < 5;
    }
};


void test(string test_name, vector<int> nums, bool expected)
{
    bool res = Solution().isStraight(nums);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {1,2,3,4,5};
    bool expected1 = true;
    test("test1", nums1, expected1);

    vector<int> nums2 = {0,0,1,2,5};
    bool expected2 = true;
    test("test2", nums2, expected2);

    vector<int> nums3 = {0,0,2,2,5};
    bool expected3 = false;
    test("test3", nums3, expected3);

    return 0;
}

// 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
// 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。
// A 不能视为 14。

// 示例 1:

// 输入: [1,2,3,4,5]
// 输出: True

// 示例 2:

// 输入: [0,0,1,2,5]
// 输出: True
//  

// 限制：
// 数组长度为 5 
// 数组的数取值为 [0, 13] .
