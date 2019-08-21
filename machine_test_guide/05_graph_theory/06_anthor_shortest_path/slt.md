### 思路1 使用dijkstra算法

根据题意，如果距离相同的话，我们还要对花费进行判断。

```cpp
#include<iostream>
#include<vector>
using namespace std;

struct Node{
    int adj;  // 邻接节点的编号
    int dist;
    int price;
};

vector<Node> path[1001];    // 注意是初始化vector的数组，而不是一个vector有1001元素

int dists[1001];         // 距离数组
int prices[1001];        // 花费数组
bool is_solved[1001];   // 是否已经在解集中

int main ()
{
    int n, m, s, t;
    while (scanf("%d %d", &n, &m) != EOF && (n || m))
    {
        for (int i = 1; i <= n; i++) path[i].clear();
        while (m--)
        {
            int a, b, d, p;
            scanf("%d%d%d%d", &a, &b, &d, &p);
            Node tmp_node;
            tmp_node.dist = d;
            tmp_node.price = p;
            tmp_node.adj = b;
            path[a].push_back(tmp_node);    // 无向图，把a到b和b到a都加入
            tmp_node.adj = a;
            path[b].push_back(tmp_node);
        }
        scanf("%d%d", &s, &t);

        // 初始化状态数组
        for (int i = 1; i <= n; i++)
        {
            dists[i] = -1;
            prices[i] = 0;
            is_solved[i] = false;
        }
        dists[s] = 0;
        is_solved[s] = true;
        int cur_node = s;

        // s已经加入，还有n-1趟
        for (int i = 0; i < n - 1; i++)
        {
            // 遍历cur_node的所有邻接点，按情况更新状态数组
            for (int j = 0; j < path[cur_node].size(); j++)
            {
                int adj_node = path[cur_node][j].adj;
                if (is_solved[adj_node]) continue;
                int dist = path[cur_node][j].dist;
                int price = path[cur_node][j].price;

                int dist_via_cur = dists[cur_node] + dist;
                int price_via_cur = prices[cur_node] + price;

                // 1.尚未计算过距离  2.之前的距离更长 3.距离相等，但是花费更小   
                // 出现上面三种情况，则更新状态数组
                if (dists[adj_node] == -1 || 
                dists[adj_node] > dist_via_cur ||
                (dists[adj_node] == dist_via_cur && prices[adj_node] > price_via_cur))
                {
                    dists[adj_node] = dist_via_cur;
                    prices[adj_node] = price_via_cur;
                }
            }

            // 当前这一趟更新完所有状态数组后，把距离最小的adj结点加入解集
            // 花费在更新状态数组的时候已经考虑到了，所以这里直接按dists数组来选择即可
            int min_dist = INT_MAX;
            for (int j = 1; j <= n; j++)
            {
                if (is_solved[j]) continue;   // 已入解集，跳过
                if (dists[j] == -1) continue; // 尚不连通，跳过
                if (dists[j] < min_dist)
                {
                    min_dist = dists[j];
                    cur_node = j;
                }
            }
            is_solved[cur_node] = true;
        }
        printf("%d %d\n", dists[t], prices[t]);
    }
    return 0;
}
```