### 思路1 使用Kruskal算法

这是一个典型的最小生成树问题。最小生成树有两种常用算法，一种是Prim算法，另一种就是Kruskal算法。它们都是基于贪心算法的解法。具体到这里是每次选择剩下边中权值最小。

下面说一下两种算法的区别：Prim算法是有点像Dijkstra算法，是每次想以连通的树加一条剩下边中权值最小的边的结点，且保证连通。又称加点法。因此其复杂度也和点相关，是O(V^2)。可以看到Prim算法适用于边稠密的图。

而Kruskal算法则是把边按权值排序，不断把当前剩下的边中权值最小的边加入，不要求加入后保持连通。又称加边法。时间复杂度为O(E*logE) （即是按边排序的时间复杂度）。Kruskal适用于边稀疏的图。

当然，如果是完全图，则不存在稠密稀疏的问题。而这道题是完全图，我们这里还是使用Kruskal算法。

```cpp
#include<iostream>
#include<vector>
using namespace std;

const int MAX_SIZE = 100;
int Tree[MAX_SIZE];

int find_root(int x)
{
    if (Tree[x] == -1) return x;
    else {
        int root = find_root(Tree[x]);
        Tree[x] = root;
        return root;
    }
}

struct Edge
{
    int a, b, weight;
    // 这里重载一定要是const函数，不然sort时报错
    bool operator < (const Edge &other) const
    {
        return weight < other.weight;
    }
};

int main()
{
    int n;
    while (scanf("%d", &n) != EOF && n != 0) {
        vector<Edge> edges;
        for (int i = 1; i <= n; i++) Tree[i] = -1;
        for (int i = 1; i <= n * (n - 1) / 2; i++) {
            Edge edge;
            scanf("%d %d %d", &edge.a, &edge.b, &edge.weight);
            edges.push_back(edge);
        }
        sort(edges.begin(), edges.end());
        int min_weight = 0;
        for (int i = 1; i <= n * (n - 1) / 2; i++) {
            // notice vector start from 0, so use i-1, i base from 1
            int a = find_root(edges[i-1].a);
            int b = find_root(edges[i-1].b);
            if (a != b) {
                Tree[a] = b;
                min_weight += edges[i-1].weight;
            }
        }
        printf("%d\n", min_weight);
    }
    return 0;
}
```