### 思路1 使用dijkstra算法

根据题意，如果距离相同的话，我们还要对花费进行判断。

```cpp
#include<iostream>
#include<vector>
using namespace std;

struct AdjNode
{
    int adj_num;
    int dist;
};

int main()
{
    int n, m, s, t;
    while (scanf("%d %d", &n, &m) != EOF && !(n == 0 && m == 0)) {
        vector<vector<AdjNode>> path(n, vector<AdjNode>());
        vector<int> dist(n, -1);
        vector<bool> is_solved(n, false);

        while (m--) {
            AdjNode node;
            int a, b, d;
            scanf("%d %d %d", &a, &b, &d);
            node.dist = d;
            node.adj_num = b;
            path[a].push_back(node);
            node.adj_num = a;
            path[b].push_back(node);
        }

        scanf("%d %d", &s, &t);
        is_solved[s] = true;
        dist[s] = 0;

        int cur_node = s;

         // s已经加入，还有n-1趟
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < path[cur_node].size(); j++) {
                int cur_adj = path[cur_node][j].adj_num;
                if (is_solved[cur_adj]) continue;
                if (
                    dist[cur_adj] == -1 ||
                    dist[cur_adj] > dist[cur_node] + path[cur_node][j].dist
                    ) {
                    dist[cur_adj] = dist[cur_node] + path[cur_node][j].dist;
                }
            }
            // 当前这一趟更新完所有状态数组后，把距离最小的adj结点加入解集
            int min_dist = INT_MAX;
            for (int j = 0; j < n; j++) {
                if (dist[j] == -1 || is_solved[j]) continue;
                if (min_dist > dist[j]) {
                    min_dist = dist[j];
                    cur_node = j;
                }
            }
            is_solved[cur_node] = true;
        }
        printf("%d\n", dist[t]);
    }
    return 0;
}
```