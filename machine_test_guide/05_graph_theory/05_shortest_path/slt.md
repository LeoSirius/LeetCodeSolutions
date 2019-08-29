### 思路1 使用Floyd算法

注意Floyd的时间复杂度是O(n^3)，如果结点数目较多，OJ使用Floyd算法可能超时。（注意path索引从0开始的）

```cpp
#include<iostream>
#include<vector>
using namespace std;

int main ()
{
    int n, m;
    while (scanf("%d %d", &n, &m) != EOF && n && m)
    {
        vector<vector<int>> path(n, vector<int>(n, -1)); // 初始化n*n的二维vector，初始值-1，表式不通
        for (int i = 1; i <= n; i++)
            path[i-1][i-1] = 0;         // 自己到自己为0

        while (m--)
        {
            int a, b, c;
            scanf("%d%d%d", &a, &b, &c);
            path[a-1][b-1] = path[b-1][a-1] = c;  // vector从0开始，是无向图，所以赋值两次
        }

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                {
                    if (path[i][k] == -1 || path[k][j] == -1)
                        continue; // 有一个不通，则直接跳过
                    if (path[i][j] == -1 || path[i][k] + path[k][j] < path[i][j])
                        path[i][j] = path[i][k] + path[k][j];
                }
        
        printf("%d\n", path[0][n-1]);
    }
    return 0;
}
```

