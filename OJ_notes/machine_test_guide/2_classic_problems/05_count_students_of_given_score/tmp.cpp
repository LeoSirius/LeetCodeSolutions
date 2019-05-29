#include<stdio.h>
using namespace std;

int Hash[101];
int main(){
    int n;
    while(scanf("%d", &n) != EOF && n != 0){
        for(int i = 0; i < n; i++){
            int tmp;
            scanf("%d", &tmp);
            Hash[tmp]++;
        }
        int m;
        scanf("%d", &m);
        printf("%d\n", Hash[m]);
    }
}