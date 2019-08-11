#include<iostream>
using namespace std;

const int SIZE = 1000;
int Tree[SIZE];

int find_root(int x){
    if(Tree[x] == -1) return x;
    else{
        int root_idx = find_root(Tree[x]);  // 这里使用了路径压缩，把这个结点直接设置成根结点的子结点
        Tree[x] = root_idx;
        return root_idx;
    }
}

int main(){
    int n, m;
    while(scanf("%d", &n) != EOF && n){
        scanf("%d", &m);
        for(int i = 1; i <= n; i++) Tree[i] = -1;  // 先初试化并查集

        while(m--){
            int a, b;
            scanf("%d %d", &a, &b);
            a = find_root(a);
            b = find_root(b);
            if(a != b) Tree[a] = b;
        }
        int num_of_connected = 0;
        for(int i = 1; i <= n; i++){
            if(Tree[i] == -1) num_of_connected++;
        }
        printf("%d\n", num_of_connected-1);
    }
    return 0;
}