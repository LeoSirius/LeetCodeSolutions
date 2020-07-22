#include <stdio.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int l = 0;
    int r = numsSize - 1;
    while (l < r) {
        int cur_sum = nums[l] + nums[r];
        if (cur_sum == target) {
            int *res = (int*)malloc(sizeof(int) * 2);
            res[0] = nums[l];
            res[1] = nums[r];
            *returnSize = 2;
            return res;
        } else if (cur_sum < target)
            l++;
        else
            r--;
    }
    return NULL;
}

/* assume two arrs' length is equal */
bool is_equal_array(int *arr1, int *arr2, int len)
{
    for (int i = 0; i < len; i++)
        if (arr1[i] != arr2[i])
            return false;
    return true;
}


void test(const char test_name[], int *nums, int numsSize, int target, int **expected)
{
    int returnSize;
    int *res = twoSum(nums, numsSize, target, &returnSize);
    bool has_target_array = false;
    for (int i = 0; i < 2; i++) {
        if (is_equal_array(expected[i], res, returnSize)) {
            has_target_array = true;
            break;
        }
    }
    if (has_target_array)
        printf("%s success.\n", test_name);
    else
        printf("%s failed.\n", test_name);
}

int main()
{
    int nums1[] = {2,7,11,15};
    int numsSize1 = 4;
    int target1 = 9;
    int arr11[] = {2,7};
    int arr21[] = {7,2};
    int *expected1[] = {arr11, arr21};
    test("test1", nums1, numsSize1, target1, expected1);

    int nums2[] = {10,26,30,31,47,60};
    int numsSize2 = 6;
    int target2 = 40;
    int arr12[] = {10, 30};
    int arr22[] = {30, 10};
    int *expected2[] = {arr12, arr22};
    test("test2", nums2, numsSize2, target2, expected2);

    return 0;
}


// 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
// 如果有多对数字的和等于s，则输出任意一对即可。

// 示例 1：
// 输入：nums = [2,7,11,15], target = 9
// 输出：[2,7] 或者 [7,2]

// 示例 2：
// 输入：nums = [10,26,30,31,47,60], target = 40
// 输出：[10,30] 或者 [30,10]
//  

// 限制：
// 1 <= nums.length <= 10^5
// 1 <= nums[i] <= 10^6