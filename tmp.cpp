#include<iostream>
using namespace std;

int
F (int num)
{
    if (num == 1) return 2;
    else return 3 * F(num - 1) + 2;
}

int
main ()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        printf("%d\n", F(n));
    }
    return 0;
}