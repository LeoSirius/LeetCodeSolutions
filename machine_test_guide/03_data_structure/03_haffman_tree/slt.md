### 思路1 利用最小堆建树

```cpp
#include<iostream>
#include<queue>
using namespace std;

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        priority_queue<int, vector<int>, greater<int>> Q;
        while (n--) {
            int x;
            scanf("%d", &x);
            Q.push(x);
        }
        int res = 0;
        while (Q.size() > 1) {
            int a = Q.top(); Q.pop();
            int b = Q.top(); Q.pop();
            res += a + b;
            Q.push(a+b);
        }
        printf("%d\n", res);
    }
}

```