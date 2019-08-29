#include<iostream>
#include<queue>
using namespace std;

bool flag[50][50][50];
int maze[50][50][50];

struct Status
{
    int x, y, z;
    int t;
};

queue<Status> Q;

int go[][3] = {
    1,0,0,
    -1,0,0,
    0,1,0,
    0,-1,0,
    0,0,1,
    0,0,-1,
};

int BFS (int a, int b, int c)
{
    while (!Q.empty()) {
        Status cur_status = Q.front(); Q.pop();
        for (int i = 0; i < 6; i++) {
            int x = cur_status.x + go[i][0];
            int y = cur_status.y + go[i][1];
            int z = cur_status.z + go[i][2];
            if (x == a-1 && y == b-1 && z == c-1) return cur_status.t + 1;

            if (x < 0 || x >= a || y < 0 || y >= b || z < 0 || z >= c) continue;
            if (maze[x][y][z] == 1) continue;
            if (flag[x][y][z] == true) continue;

            Status new_status;
            new_status.x = x;
            new_status.y = y;
            new_status.z = z;
            new_status.t = cur_status.t + 1;
            Q.push(new_status);
            flag[x][y][z] = true;
        }
    }
    return -1;
}

int main ()
{
    int k;
    scanf("%d", &k);
    while (k--) {
        int a, b, c, t;
        scanf("%d %d %d %d", &a, &b, &c, &t);
        for (int x = 0; x < a; x++) {
            for (int y = 0; y < b; y++) {
                for (int z = 0; z < c; z++) {
                    scanf("%d", &maze[x][y][z]);
                    flag[x][y][z] = false;
                }
            }
        }
        while (!Q.empty()) Q.pop();
        flag[0][0][0] = true;
        Status init_status;
        init_status.x = init_status.y = init_status.z = init_status.t = 0;
        Q.push(init_status);

        int res = BFS(a, b, c);
        if (res <= t) printf("%d\n", res);
        else printf("-1\n");
    }
    return 0;
}