#include<iostream>
using namespace std;

const int SIZE = 10000001;
int Tree[SIZE];
int num_of_connected[SIZE];

int
find_root (int x)
{
    if (Tree[x] == -1) return x;
    else {
        int root = find_root(Tree[x]);
        Tree[x] = root;
        return root;
    }
}

int
main ()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        for (int i = 1; i <= SIZE; i++) {
            Tree[i] = -1;
            num_of_connected[i] = 1;
        }

        while (n--) {
            int a, b;
            scanf("%d %d", &a, &b);
            a = find_root(a);
            b = find_root(b);
            if (a != b) {
                Tree[a] = b;
                num_of_connected[b] += num_of_connected[a];
            }
        }

        int max_node_cnt = INT_MIN;
        for (int i = 1; i <= SIZE; i++) {
            if (Tree[i] == -1 && max_node_cnt < num_of_connected[i])
                max_node_cnt = num_of_connected[i];
        }

        printf("%d\n", max_node_cnt);
    }
    return 0;
}