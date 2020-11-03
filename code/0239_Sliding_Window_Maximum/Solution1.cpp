#include <iostream>
#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> deq;
        vector<int> res;

        for (int i = 0; i < nums.size(); i++) {
            //新元素入队时如果比队尾元素大的话就替代队尾元素
            while (!deq.empty() && nums[deq.back()] < nums[i])
                deq.pop_back();

            //检查队首的index是否在窗口内，不在的话需要出队
            if (!deq.empty() && deq.front() < i - k + 1)
                deq.pop_front();
            deq.push_back(i);

            // 索引i遍历到满足条件时，直接每次把deq的第一个元素加到res里就好了
            if (k - 1 <= i)
                res.push_back(nums[deq.front()]);
        }
        return res;
    }
};

void test(string test_name, vector<int> nums, int k, vector<int> expected)
{
    vector<int> res = Solution().maxSlidingWindow(nums, k);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {1,3,-1,-3,5,3,6,7};
    int k1 = 3;
    vector<int> expected1 = {3,3,5,5,6,7};
    test("test1", nums1, k1, expected1);

    return 0;
}



// 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

// 示例:

// 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
// 输出: [3,3,5,5,6,7] 
// 解释: 

//   滑动窗口的位置                最大值
// ---------------               -----
// [1  3  -1] -3  5  3  6  7       3
//  1 [3  -1  -3] 5  3  6  7       3
//  1  3 [-1  -3  5] 3  6  7       5
//  1  3  -1 [-3  5  3] 6  7       5
//  1  3  -1  -3 [5  3  6] 7       6
//  1  3  -1  -3  5 [3  6  7]      7
//  

// 提示：

// 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

