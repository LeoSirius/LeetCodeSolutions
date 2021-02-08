#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findContinuousSequence(int target, int* returnSize, int** returnColumnSizes){
    int **res = (int**)malloc(sizeof(int*) * target);
    int *col = (int*)malloc(sizeof(int)*target);

    int col_p = 0;
    int res_p = 0;
    for (int start = 1; start < target; start++) {
        int p = start;
        int cur_sum = p;
        while (cur_sum < target) {
            p++;
            cur_sum += p;
        }
        // printf("start = %d, cur_sum = %d, p = %d\n", start, cur_sum, p);
        if (cur_sum == target) {
            int len = p - start + 1;
            int *path = (int*)malloc(sizeof(int) * len);
            for (int i = 0; i < len; i++)
                path[i] = start + i;
            col[col_p++] = len;
            res[res_p++] = path;
        }
    }
    // for (int i = 0; i < col_p; i++)
    //     printf("col[i] = %d\n", col[i]);
    // printf("222\n");
    *returnColumnSizes = col;
    // printf("333\n");
    *returnSize = res_p;
    // printf("444\n");
    return res;
}

void test(const char test_name[], int target, int **expected)
{
    int *returnSize;
    int **returnColumnSizes;
    printf("000\n");
    int **res;
    res = findContinuousSequence(target, returnSize, returnColumnSizes);
    printf("111\n");
    bool pass = true;
    for (int i = 0; i < *returnSize; i++) {
        printf("i = %d, *returnColumnSizes[i] = %d\n", i, (*returnColumnSizes)[i]);
        for (int j = 0; j < (*returnColumnSizes)[i]; j++) {
            printf("in in in j = %d\n", j);
            if (res[i][j] != expected[i][j]) {
                pass = false;
                break;
            }
        }
    }
    if (pass)
        printf("%s success.\n", test_name);
    else
        printf("%s failed.\n", test_name);
}

int main()
{
    int target1 = 9;
    int arr11[] = {2,3,4};
    int arr21[] = {4,5};
    int *expected1[] = {arr11, arr21};
    test("test1", target1, expected1);

    int target2 = 15;
    int arr12[] = {1,2,3,4,5};
    int arr22[] = {4,5,6};
    int arr32[] = {7,8};
    int *expected2[] = {arr12, arr22, arr32};
    test("test2", target2, expected2);

    return 0;
}

// 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

// 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

//  

// 示例 1：

// 输入：target = 9
// 输出：[[2,3,4],[4,5]]
// 示例 2：

// 输入：target = 15
// 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
//  

// 限制：

// 1 <= target <= 10^5