#include<iostream>
#include<cmath>
using namespace std;

bool is_prime(int x)
{
    int sqrtx = sqrt(x);
    for (int i = 2; i <= sqrtx; i++) {
        if (x % i == 0) return false;
    }
    return true;
}

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        is_prime(n) ? printf("yes\n") : printf("no\n");
    }
    return 0;
}