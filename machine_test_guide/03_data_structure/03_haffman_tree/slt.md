### 思路1 利用最小堆建树

```cpp
#include<iostream>
#include<queue>
using namespace std;

int main(){
    // 一个小顶堆
    priority_queue<int, vector<int>, greater<int>> Q;
    int n;
    while(scanf("%d", &n) != EOF){
        while(!Q.empty()) Q.pop();
        for(int i = 0; i < n; ++i){
            int temp;
            scanf("%d", &temp);
            Q.push(temp);
        }
        int res = 0;
        while(Q.size() > 1){
            int a, b;
            a = Q.top(); Q.pop();
            b = Q.top(); Q.pop();
            res += a + b;
            Q.push(a+b);
        }
        printf("%d\n", res);
    }
    return 0;
}
```