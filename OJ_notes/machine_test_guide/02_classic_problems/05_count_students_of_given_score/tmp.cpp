#include<iostream>
using namespace std;

int hashing[101];

int main(){
    int n;
    while(scanf("%d", &n) != EOF and n != 0){
        for(int i = 0; i < n; i++){
            hashing[i] = 0;
        }
        int score;
        for(int i = 0; i < n; i++){
            scanf("%d", &score);
            hashing[score]++;
        }
        int target_socre;
        scanf("%d", &target_socre);
        printf("%d\n", hashing[target_socre]);
    }
    return 0;
}