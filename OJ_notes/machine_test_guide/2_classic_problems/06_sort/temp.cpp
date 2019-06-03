#include<stdio.h>
#define OFFSET 500000
using namespace std;

int Hash[1000001];

int main(){
    int n, m;
    while(scanf("%d%d", &n, &m) != EOF){
        int input;
        for(int i = 0; i < n; i++){
            scanf("%d", &input);
            Hash[OFFSET + input] = 1;
        }
        for(int i = 500000; i >= -500000; i--){
            if(Hash[i+OFFSET]){
                m--;
                printf("%d", i);
                if(m != 0){
                    printf(" ");
                }else{
                    printf("\n");
                    break;
                }
            }
        }
    }
}