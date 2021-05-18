#include <stdio.h>
#include <stdbool.h>

bool divisorGame(int n)
{
    return n % 2 == 0;
}

void test(const char *test_name, int n, bool expected)
{
    bool res = divisorGame(n);
    if (res == expected) {
        printf("%s success.\n", test_name);
    } else {
        printf("%s failed.\n", test_name);
    }
}

int main()
{
    int n1 = 2;
    bool expected1 = true;
    test("test1", n1, expected1);

    int n2 = 3;
    bool expected2 = false;
    test("test2", n2, expected2);

    int n3 = 4;
    bool expected3 = true;
    test("test3", n3, expected3);

    return 0;
}

// Example 1:

// Input: n = 2
// Output: true
// Explanation: Alice chooses 1, and Bob has no more moves.
// Example 2:

// Input: n = 3
// Output: false
// Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

