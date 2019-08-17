### 思路1 Kruskal算法求MST权值

与上一题不同之处在于，这道题要先自己把坐标转化为结点及边。

```cpp
#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;

const int N = 101;
int Tree[N];

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

struct Edge
{
    int a, b;
    double weight;
    bool operator < (const Edge& B) const
    {
        return weight < B.weight;
    }
};

struct Point
{
    double x, y;
    double get_distance (Point& B)
    {
        return sqrt((x-B.x) * (x-B.x) + (y-B.y) * (y-B.y));
    }
};

int main(){
    int n;
    while (scanf("%d", &n) != EOF)
    {
        vector<Point> points;
        vector<Edge> edges;
        for (int i = 0; i < n; i++)
        {
            Point new_point;
            scanf("%lf %lf", &new_point.x, &new_point.y);
            points.push_back(new_point);
        }

        // 下面各个结点的编号就是vector的索引加1，从1到n
        for (int i = 1; i <= n; i++)
        {
            for (int j = i + 1; j <= n; j++)
            {
                Edge new_edge;
                new_edge.a = i; new_edge.b = j;
                new_edge.weight = points[i-1].get_distance(points[j-1]);
                edges.push_back(new_edge);
            }
        }
        sort(edges.begin(), edges.end());
        for (int i = 1; i <= n; i++) Tree[i] = -1;

        double res = 0;
        for (int i = 0; i < edges.size(); i++)
        {
            int a = find_root(edges[i].a);
            int b = find_root(edges[i].b);
            if (a != b)
            {
                Tree[a] = b;
                res += edges[i].weight;
            }
        }
        printf("%.2lf\n", res);
    }
    return 0;
}
```