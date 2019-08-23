### 思路1 求个质因数的幂次和

以120为例，可以分解为2 * 2 * 2 * 3 * 5。

任何一个合数都能被一个比它小的质数整除。所以当我们用小质数去分解这个给定的数时，我们已经把他的合数因子分解了。所以这道题不用判断质数。

```cpp
#include<iostream>
#include<cmath>
using namespace std;

int main ()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        int count = 0;
        int sqrt_n = sqrt(n);
        for (int i = 2; i <= sqrt_n; i++) {
            while (n % i == 0) {
                n /= i;
                count++;
            }
            if (n <= 1) break;
        }
        if (n > 1) count++;    // 还没有分解到1，且没有质因数了，说明这时的n自己就是质数。
        printf("%d\n", count);
    }
    return 0;
}
```