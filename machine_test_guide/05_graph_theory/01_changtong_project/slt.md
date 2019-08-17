### 思路1 使用并查集

首先确定一点，把n个结点连通，最少需要n-1个边。在这题中，我们先根据已经有的道路，计算出已有的连通分量的个数，这个值减1，就是要求的最少还需要的道路的数目。

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