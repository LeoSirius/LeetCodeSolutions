#include<iostream>
using namespace std;

int f(int n)
{
    if (n == 1) return 2;
    else {
        return 3 * f(n-1) + 2;
    }
}

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        printf("%d\n", f(n));
    }
    return 0;
}