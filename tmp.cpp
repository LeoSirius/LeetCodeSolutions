#include<iostream>
using namespace std;

const int OFFSET = 500000;

int main(){
    int n, m;
    while(scanf("%d %d", &n, &m) != EOF){
        int *hashing = new int[1000001]{0};
        for(int i = 0; i < n; i++){
            int x;
            scanf("%d", &x);
            hashing[x+OFFSET] = 1;
        }
        for(int i = 500000; i >= -500000; i--){
            if(hashing[i+OFFSET]){
                printf("%d", i);
                m--;
                if(m){
                    printf(" ");
                }else{
                    printf("\n");
                    break;
                }
            }
        }
        delete [] hashing;
    }
}