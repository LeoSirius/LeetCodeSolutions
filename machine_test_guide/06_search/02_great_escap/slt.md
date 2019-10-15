### 思路1 BFS

```c
#include<iostream>
#include<queue>
#include<vector>
using namespace std;

typedef vector<vector<vector<int>>> vector_3d;

// 状态结构体，表示走到(x,y,z)用了时间t
struct Status
{
    int x, y, z, t;
    Status(int x, int y, int z, int t): x(x), y(y), z(z), t(t) {}
};

int go[][3] = {
    1,0,0,
    -1,0,0,
    0,1,0,
    0,-1,0,
    0,0,1,
    0,0,-1,
};

int BFS(int a, int b, int c, queue<Status> &Q, vector_3d &maze, vector_3d flag)
{
    while (!Q.empty()) {
        Status cur_status = Q.front(); Q.pop();
        for (int i = 0; i < 6; i++) {
            int x = cur_status.x + go[i][0];
            int y = cur_status.y + go[i][1];
            int z = cur_status.z + go[i][2];

            // 如果已经到终点，则返回时间
            if (x == a - 1 && y == b - 1 && z == c - 1) return cur_status.t + 1;

            // 超出范围，或者是墙，或者已经走过，则跳过
            if (x < 0 || x >= a || y < 0 || y >= b || z < 0 || z >= c) continue;
            if (maze[x][y][z] == 1 || flag[x][y][z]) continue;

            Status new_status(x, y, z, cur_status.t + 1);
            Q.push(new_status);
            flag[x][y][z] = true;
        }
    }
    return -1;
}

int main()
{
    int k;
    scanf("%d", &k);
    while (k--) {
        int a, b, c, t;
        scanf("%d %d %d %d", &a, &b, &c, &t);
        // 初始化maze和flag， flag中为false表示未走过
        vector_3d flag(a, vector<vector<int>>(b, vector<int>(c, false)));
        vector_3d maze(a, vector<vector<int>>(b, vector<int>(c)));
        for (int x = 0; x < a; x++)
            for (int y = 0; y < b; y++)
                for (int z = 0; z < c; z++)
                    scanf("%d", &maze[x][y][z]);
        
        queue<Status> Q;
        Status init_status(0, 0, 0, 0);
        Q.push(init_status);
        int res = BFS(a, b, c, Q, maze, flag);
        if (res != -1 && res <= t)
            printf("%d\n", res);
        else
            printf("-1\n");
    }
    return 0;
}
```