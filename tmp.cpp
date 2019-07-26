#include<iostream>
using namespace std;

int main(){
    int n;
    while(scanf("%d", &n) != EOF && n){
        int *hashing = new int[101]{0};
        for(int i = 0; i < n; i++){
            int x;
            scanf("%d", &x);
            hashing[x]++;
        }
        int target_score;
        scanf("%d", &target_score);
        printf("%d\n", hashing[target_score]);
        delete [] hashing;
    }
    return 0;
}