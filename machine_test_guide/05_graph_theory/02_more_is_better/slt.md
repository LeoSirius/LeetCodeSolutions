### 思路1 利用并查集求得线最大连通分量的结点个数

```cpp
#include<iostream>
using namespace std;

const int N = 10000001;
int Tree[N];
// sum[i]表示以结点i为根的树的结点个数，即结点i所在的连通分量的结点个数，
// 其中保存的数据仅当Tree[i] = -1,即该结点为树的根结点时有效
int sum[N];


int find_root (int x)
{
    if (Tree[x] == -1) return x;
    else {
        int root = find_root(Tree[x]);
        Tree[x] = root;
        return root;
    }
}

int main ()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        for (int i = 1; i < N; i++ ) {
            Tree[i] = -1;
            sum[i] = 1;
        }
        while (n--) {
            int a, b;
            scanf("%d %d", &a, &b);
            a = find_root(a);
            b = find_root(b);
            if (a != b) {
                Tree[a] = b;        // 将a树并到b树中
                sum[b] += sum[a];   // 并将sum结点的计数加到b的sum中
            }
        }
        int res = 1;
        for (int i = 1; i < N; i++) 
            if (Tree[i] == -1 && res < sum[i])
                res = sum[i];
        printf("%d\n", res);
    }
    return 0;
}
```