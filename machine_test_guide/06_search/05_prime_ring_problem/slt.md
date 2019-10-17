### 思路1 使用DFS

我们用回溯法枚举每一个值。第一个数已经确定为1，我们再枚举后面的每个数，使两个相邻的数和为素数即可。

```c++
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

bool is_prime(int n)
{
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

void check_print(vector<int> &ring)
{
    int size = ring.size();
    // 要同时检查最后两个元素和首尾两个元素
    if (!is_prime(ring[0] + ring[size-1]) || !is_prime(ring[size-1] + ring[size-2]))
        return;
    for (int i = 0; i < size; i++) {
        printf("%d ", ring[i]);
    }
    printf("\n");
}

void DFS(int n, vector<int> &ring, vector<bool> &is_in)
{
    int size = ring.size();
    if (size == n) check_print(ring);
    if (size > 1 && !is_prime(ring[size-1] + ring[size-2])) return;   // 检查环中最后两个数是否满足条件，从DFS第二次被调用开始检查
    for (int i = 2; i <= n; i++) {
        if (!is_in[i]) {
            is_in[i] = true;
            ring.push_back(i);
            DFS(n, ring, is_in);
            ring.pop_back();
            is_in[i] = false;
        }
    }
}

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        vector<int> ring(1, 1);
        vector<bool> is_in(n + 1, false);
        is_in[0] = true;
        DFS(n, ring, is_in);
        printf("\n");
    }
    return 0;
}

```