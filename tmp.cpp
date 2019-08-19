#include<algorithm>
using namespace std;

const int SIZE = 1001;
int Tree[SIZE];
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

int main ()
{
    int n, m;
    while (scanf("%d %d", &n, &m) != EOF && n)
    {
        for (int i = 1; i <= n; i++) Tree[i] = -1;
        while (m--)
        {
            int a, b;
            scanf("%d %d", &a, &b);
            a = find_root(a);
            b = find_root(b);
            if (a != b) Tree[a] = b;
        }

        int num_of_connected = 0;
        for (int i = 1; i <= n; i++)
            if (Tree[i] == -1) num_of_connected++;

        printf("%d\n", num_of_connected - 1);
    }
    return 0;
}