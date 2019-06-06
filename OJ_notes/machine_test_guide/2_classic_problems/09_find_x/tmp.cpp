#include<stdio.h>
using namespace std;

int main(){
    int buf[200];
    int n;
    while(scanf("%d", &n) != EOF){
        for(int i = 0; i < n; i++){
            scanf("%d", &buf[i]);
        }
        int x;
        scanf("%d", &x);
        for(int i = 0; i < n; i++){
            if(x == buf[i]){
                printf("%d\n", i);
            }
        }
        printf("-1\n");
    }
    return -1;
}