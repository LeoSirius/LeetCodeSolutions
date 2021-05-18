#include <stdio.h>

#define INT_ARR_SIZE(arr) (sizeof(arr)/sizeof(int))
#define MIN(a, b) (a < b ? a : b)

int minCostClimbingStairs(int* cost, int costSize)
{
    for (int i = 2; i < costSize; i++) {
        cost[i] += MIN(cost[i-1], cost[i-2]);
    }
    return MIN(cost[costSize-2], cost[costSize-1]);
}

void test(const char *test_name, int *cost, int costSize, int expected)
{
    int res = minCostClimbingStairs(cost, costSize);
    if (res == expected) {
        printf("%s success.\n", test_name);
    } else {
        printf("%s failed.\n", test_name);
    }
}

int main()
{
    int cost1[] = {10,15,20};
    int expected1 = 15;
    test("test1", cost1, INT_ARR_SIZE(cost1), expected1);

    int cost2[] = {1,100,1,1,1,100,1,1,100,1};
    int expected2 = 6;
    test("test2", cost2, INT_ARR_SIZE(cost2), expected2);

    return 0;
}
