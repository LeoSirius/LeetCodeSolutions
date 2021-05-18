#include <stdio.h>

#define INT_ARR_SIZE(arr)  sizeof(arr)/sizeof(int)

int countTriplets(int* arr, int arrSize)
{
    if (arrSize < 2) return 0;

    int i, j, k = 0;
    int prexor[arrSize+1];
    int res = 0;
    prexor[0] = 0;

    for (i = 1; i <= arrSize; i++)
        prexor[i] = prexor[i-1] ^ arr[i-1];
    
    for (i = 0; i < arrSize; i++) {
        for (k = i + 1; k < arrSize; k++) {
            if (prexor[i] == prexor[k+1]) {
                res += k - i;
            }
        }
    }
    return res;
}

void test(const char *test_name, int *arr, int arrSize, int expected)
{
    int res = countTriplets(arr, arrSize);
    if (res == expected) {
        printf("%s success.\n", test_name);
    } else {
        printf("%s failed.\n", test_name);
    }
}

int main()
{
    int arr1[] = {2,3,1,6,7};
    int expected1 = 4;
    test("test1", arr1, INT_ARR_SIZE(arr1), expected1);

    int arr2[] = {1,1,1,1,1};
    int expected2 = 10;
    test("test2", arr2, INT_ARR_SIZE(arr2), expected2);

    int arr3[] = {2,3};
    int expected3 = 0;
    test("test3", arr3, INT_ARR_SIZE(arr3), expected3);

    int arr4[] = {1,3,5,7,9};
    int expected4 = 3;
    test("test4", arr4, INT_ARR_SIZE(arr4), expected4);

    int arr5[] = {7,11,12,9,5,2,7,17,22};
    int expected5 = 8;
    test("test5", arr5, INT_ARR_SIZE(arr5), expected5);

    int arr6[] = {218,218};
    int expected6 = 1;
    test("test6", arr6, INT_ARR_SIZE(arr6), expected6);

    return 0;
}
