#include<iostream>
using namespace std;

int main(){
    int n;
    int inputs[200];
    while(scanf("%d", &n) != EOF){
        for(int i = 0; i < n; i++){
            scanf("%d", &inputs[i]);
        }
        int x;
        scanf("%d", &x);
        for(int i = 0; i < n; i++){
            if(x == inputs[i]){
                printf("%d\n", i);
                break;
            }
            if(i == n - 1){
                printf("-1\n");
            }
        }
    }
    return 0;
}