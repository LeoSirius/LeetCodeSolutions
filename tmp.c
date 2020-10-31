#include <stdio.h>
#include "meta_c/utils.h"

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxSlidingWindow(int* nums, int numsSize, int k, int* returnSize){

}

void test(const char *test_name, int* nums, int numsSize, int k, int *expected)
{
    int *return_size;
    int *res = maxSlidingWindow(nums, numsSize, k, return_size);
    if (is_equal_array(res, expected, return_size))
        printf("%s success.\n", test_name);
    else
        printf("%s failed.\n", test_name);
}


int main()
{
    int nums1 = {1,3,-1,-3,5,3,6,7};
    int k1 = 3;
    int expected1 = {3,3,5,5,6,7};
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
