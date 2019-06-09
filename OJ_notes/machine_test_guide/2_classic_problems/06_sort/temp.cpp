#include<iostream>
using namespace std;

#define OFFSET 500000
int buf[1000001];

int main(){
    int n, m;
    while(scanf("%d%d", &n, &m) != EOF){
        int tmp;
        for(int i = 0; i < n; i++){
            scanf("%d", &tmp);
            buf[tmp+OFFSET] = 1;
        }
        for(int i = 500000; i >= -500000; i--){
            if(buf[i+OFFSET] != 0){
                printf("%d", i);
                m--;
                if(m != 0){
                    printf(" ");
                }else{
                    printf("\n");
                    break;
                }
            }
        }
    }
    return 0;
}