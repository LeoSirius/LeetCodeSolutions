#include<stdio.h>
#define OFFSET 500000
int Hash[1000001];          // 下标对应的数，出现标记为1，否则为0

int main(){
    int n, m;
    while(scanf("%d%d", &n, &m) != EOF){
        for(int i = 0; i < n; i++){
            int x;
            scanf("%d", &x);
            Hash[x+OFFSET] = 1;
        }
        for(int i = 500000; i >= -500000; i--){
            if(Hash[i+OFFSET] == 1){
                printf("%d", i);
                m--;
                if(m != 0)          // 这里加各式控制，最后一个数后面没有空格
                    printf(" ");
                else{
                    printf("\n");
                    break;
                }
            }
        }
    }
}