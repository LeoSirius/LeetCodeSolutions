#include<iostream>
using namespace std;

int gcd(int a, int b)
{
    return b == 0 ? a : gcd(b, a % b);
}

int main()
{
    int a, b;
    while (scanf("%d %d", &a, &b) != EOF) {
        printf("%d\n", a * b / gcd(a, b));
    }
    return 0;
}