#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        bool is_prime = true;
        for (int i = 2; i <= sqrt(n); i++) {
            if (n % i == 0) {
                is_prime = false;
            }
        }
        if (is_prime)
            printf("yes\n");
        else
            printf("no\n");
    }
    return 0;
}