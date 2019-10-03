### 思路1 使用并查集

首先确定一点，把n个结点连通，最少需要n-1个边。在这题中，我们先根据已经有的道路，计算出已有的连通分量的个数，这个值减1，就是要求的最少还需要的道路的数目。

在find_root函数中，我们使用了路径压缩。

```cpp
#include<algorithm>
using namespace std;

const int SIZE = 1001;
int Tree[SIZE];
int find_root (int x)
{
    if (Tree[x] == -1) return x;
    else
    {
        int root = find_root(Tree[x]);
        Tree[x] = root;
        return root;
    }
    
}

int main ()
{
    int n, m;
    while (scanf("%d %d", &n, &m) != EOF && n)
    {
        for (int i = 1; i <= n; i++) Tree[i] = -1;
        while (m--)
        {
            int a, b;
            scanf("%d %d", &a, &b);
            a = find_root(a);
            b = find_root(b);
            if (a != b) Tree[a] = b;
        }

        int num_of_connected = 0;
        for (int i = 1; i <= n; i++)
            if (Tree[i] == -1) num_of_connected++;

        printf("%d\n", num_of_connected - 1);
    }
    return 0;
}
```