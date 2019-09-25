#include<iostream>
#include<vector>
using namespace std;

void init_primes(int n, vector<bool> &is_prime)
{
    for (int i = 2; i < n; i++) {
        if (!is_prime[i]) continue;
        for (int j = i * i; j <= n; j += i) {
            is_prime[j] = false;
        }
    }

}

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        vector<bool> is_prime(n+1, true);
        init_primes(n, is_prime);
        bool has_res = false;
        for (int i = 2; i < n; i++) {
            if (i % 10 == 1 && is_prime[i]) {
                has_res = true;
                printf("%d ", i);
            }
        }
        if(!has_res) printf("-1");
        printf("\n");
    }
    return 0;
}