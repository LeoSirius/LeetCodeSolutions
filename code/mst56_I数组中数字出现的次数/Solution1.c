#include <stdio.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumbers(int* nums, int numsSize, int* returnSize){
    unsigned int bitmap = 0;
    for (int i = 0; i < numsSize; i++)
        bitmap ^= nums[i];

    int idx = 1;
    while ((bitmap & 1) == 0) {
        bitmap >>= 1;
        idx++;
    }

    int r1, r2;
    r1 = r2 = 0;
    for (int i = 0; i < numsSize; i++) {
        if ((nums[i] >> (idx - 1) & 1) == 0)
            r1 ^= nums[i];
        else
            r2 ^= nums[i];
    }
    int *res = (int*)malloc(2 * sizeof(int));
    res[0] = r1;
    res[1] = r2;
    *returnSize = 2;
    return res;
}

/* assume two arrs' length is equal */
bool is_equal_array(int *arr1, int *arr2, int len)
{
    for (int i = 0; i < len; i++)
        if (arr1[i] != arr2[i])
            return false;
    return true;
}

void test(const char test_name[], int *nums, int numsSize, int *expected[])
{
    int returnSize;
    int *res;
    res = singleNumbers(nums, numsSize, &returnSize);
    bool has_target_array = false;
    for (int i = 0; i < 2; i++) {
        if (is_equal_array(res, expected[i], 2)) {
            has_target_array = true;
            break;
        }
    }
    if (has_target_array && returnSize == 2)
        printf("%s success.\n", test_name);
    else
        printf("%s failed.\n", test_name);
    free(res);
}

int main()
{
    int nums1[] = {4,1,4,6};
    int numsSize1 = 4;
    int arr11[] = {1,6};
    int arr21[] = {6,1};
    int *expected1[] = {arr11, arr21};
    test("test1", nums1, numsSize1, expected1);

    int nums2[] = {1,2,10,4,1,4,3,3};
    int numsSize2 = 8;
    int arr12[] = {2,10};
    int arr22[] = {10,2};
    int *expected2[] = {arr12, arr22};
    test("test2", nums2, numsSize2, expected2);

    return 0;
}


//  一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
//  要求时间复杂度是O(n)，空间复杂度是O(1)。

//  示例 1：
//  输入：nums = [4,1,4,6]
//  输出：[1,6] 或 [6,1]

//  示例 2：
//  输入：nums = [1,2,10,4,1,4,3,3]
//  输出：[2,10] 或 [10,2]

//  限制：
//  2 <= nums.length <= 10000
