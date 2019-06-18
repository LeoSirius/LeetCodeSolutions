#include<stdio.h>
int main(){
    int buf[200];
    int n;
    while(scanf("%d", &n) != EOF){
        for(int i = 0; i < n; i++){
            scanf("%d", &buf[i]);
        }
        int x, res = -1;
        scanf("%d", &x);
        for(int i = 0; i < n; i++){
            if(x == buf[i]){
                res = i;
                break;
            }
        }
        printf("%d\n", res);
    }
    return 0;
}