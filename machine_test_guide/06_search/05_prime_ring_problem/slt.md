### 思路1 使用DFS

我们用回溯法枚举每一个值。第一个数已经确定为1，我们再枚举后面的每个数，使两个相邻的数和为素数即可。

```c++
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

bool is_prime(int num)
{
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}


void check_print(int n, vector<int> &ring)
{
    int size = ring.size();
    // k == n的时候，要同时检查最后两个元素和首尾两个元素
    if (!is_prime(ring[0] + ring[size - 1]) ||
        !is_prime(ring[size-1] + ring[size-2])
    ) return;
    for (int i = 0; i < ring.size(); i++) {
        printf("%d ", ring[i]);
    }
    printf("\n");
}

// 用k来表示递归测层数，k == n时，即把n个数都放在了环里，这时检查首尾两个数，并输出
void DFS(int k, int n, vector<int> &ring, vector<bool> &is_in)
{
    if (k == n) {
        check_print(n, ring);
        return;
    }
    int size = ring.size();
    // 检查环中最后两个数是否满足条件，从DFS第二次被调用开始检查
    if (k > 1 && !is_prime(ring[size-1] + ring[size-2])) return;

    for (int i = 2; i <= n; i++) {
        if(!is_in[i]) {
            is_in[i] = true;
            ring.push_back(i);
            DFS(k+1, n, ring, is_in);
            ring.pop_back();
            is_in[i] = false;
        }
    }
}

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        vector<int> ring;
        vector<bool> is_in(n + 1, false);    // 为方便，我们从1开始
        ring.push_back(1);
        is_in[1] = true;
        DFS(1, n, ring, is_in);
        printf("\n");
    }
    return 0;
}
```