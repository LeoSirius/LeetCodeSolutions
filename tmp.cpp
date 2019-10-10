#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int n, m;
    while (scanf("%d %d", &n, &m) != EOF && !(n == 0 && m == 0)) {
        vector<vector<int>> path(n, vector<int>(n, -1));
        for (int i = 0; i < n; i++)
            path[i][i] = -1;

        while (m--) {
            int a, b, c;
            scanf("%d %d %d", &a, &b, &c);
            path[a-1][b-1] = path[b-1][a-1] = c;
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (path[i][k] == -1 || path[k][j] == -1) continue;
                    if (path[i][j] == -1 || path[i][j] > path[i][k] + path[k][j])
                        path[i][j] = path[i][k] + path[k][j];
                }
            }
        }
        printf("%d\n", path[0][n-1]);
    }
    return 0;
}