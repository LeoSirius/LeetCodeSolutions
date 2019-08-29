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
    int price;
};

vector<AdjNode> path[1001];

int dists[1001];
int prices[1001];
bool is_solved[1001];

int main ()
{
    int n, m, s, t;
    while (scanf("%d %d", &n, &m) != EOF && !(n == 0 && m == 0)) {
        for (int i = 1; i <= n; i++) path[i].clear();
        while (m--) {
            int a, b, d, p;
            scanf("%d %d %d %d", &a, &b, &d, &p);
            AdjNode node;
            node.dist = d;
            node.price = p;
            node.adj_num = b;
            path[a].push_back(node);
            node.adj_num = a;
            path[b].push_back(node);
        }

        for (int i = 1; i <= n; i++)
        {
            dists[i] = -1;
            prices[i] = 0;
            is_solved[i] = false;
        }

        scanf("%d %d", &s, &t);
        dists[s] = 0;
        is_solved[s] = true;
        int cur_node = s;

        // s已经加入，还有n-1趟
        for (int i = 0; i < n - 1; i++) {
            // 遍历cur_node的所有邻接点，按情况更新状态数组
            for (int j = 0; j < path[cur_node].size(); j++) {
                int adj_num = path[cur_node][j].adj_num;
                int cur_2_adj_dist = path[cur_node][j].dist;
                int cur_2_adj_price = path[cur_node][j].price;
                
                if (is_solved[adj_num]) continue;

                int dist_via_cur = dists[cur_node] + cur_2_adj_dist;
                int price_via_cur = prices[cur_node] + cur_2_adj_price;

                // 1.尚未计算过距离  2.之前的距离更长 3.距离相等，但是花费更小   
                // 出现上面三种情况，则更新状态数
                if (dists[adj_num] == -1 ||
                    dists[adj_num] > dist_via_cur ||
                    (dists[adj_num] == dist_via_cur && (prices[adj_num] > price_via_cur))) {
                    dists[adj_num] = dist_via_cur;
                    prices[adj_num] = price_via_cur;
                }
            }

            // 当前这一趟更新完所有状态数组后，把距离最小的adj结点加入解集
            // 花费在更新状态数组的时候已经考虑到了，所以这里直接按dists数组来选择即可
            int min_dist = INT_MAX;
            for (int j = 1; j <= n; j++) {
                if (is_solved[j] || dists[j] == -1) continue;
                if (min_dist > dists[j]) {
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