### 思路1 开方后遍历

```cpp
#include<cmath>
using namespace std;

bool is_prime(int x)
{
    int sqrt_x = sqrt(x);
    for (int i = 2; i <= sqrt_x; i++) {
        if (x % i == 0) return false;
    }
    return true;
}

int main ()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        is_prime(n) ? printf("yes\n") : printf("no\n");
    }
    return 0;
}
```