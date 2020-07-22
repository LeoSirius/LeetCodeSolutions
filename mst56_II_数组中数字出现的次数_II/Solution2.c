#include <stdio.h>

int singleNumber(int* nums, int numsSize){
    int digits_cnt[32] = {0};
    for (int i = 0; i < numsSize; i++) {
        unsigned int n = nums[i];
        for (int i = 0; i < 32; i++) {
            if (((n >> i) & 1) == 1)
                digits_cnt[i]++;
            digits_cnt[i] %= 3;
        }
    }

    int res = 0;
    // for会loop32次，第一次后base是2, 即2的1次方
    // 最后一次是 4294967296 是 2的32 次方，直接用int在32位机器上会溢出
    // 或者另一种改法，在第32次循环的时候跳过，不让base *= 2
    long base = 1;
    for (int i = 0; i < 32; i++) {
        res = res + digits_cnt[i] * base;
        base *= 2;
    }
    return res;
}


void test(const char test_name[], int *nums, int numsSize, int expected)
{
    int res = singleNumber(nums, numsSize);
    if (res == expected)
        printf("%s success.\n", test_name);
    else
        printf("%s failed.\n", test_name);
}


int main()
{
    int nums1[] = {3,4,3,3};
    int numsSize1 = 4;
    int expected1 = 4;
    test("test1", nums1, numsSize1, expected1);

    int nums2[] = {9,1,7,9,7,9,7};
    int numsSize2 = 7;
    int expected2 = 1;
    test("test2", nums2, numsSize2, expected2);

    int nums3[] = {3,4,3,3};
    int numsSize3 = 4;
    int expected3 = 4;
    test("test3", nums3, numsSize3, expected3);
}

// 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。
// 请找出那个只出现一次的数字。

// 示例 1：

// 输入：nums = [3,4,3,3]
// 输出：4


// 示例 2：
// 输入：nums = [9,1,7,9,7,9,7]
// 输出：1
//  

// 限制：

// 1 <= nums.length <= 10000
// 1 <= nums[i] < 2^31
