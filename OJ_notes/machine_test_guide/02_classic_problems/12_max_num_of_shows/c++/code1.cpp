#include<iostream>
#include<algorithm>
using namespace std;

struct Show{
    int s_time, e_time;
    bool operator < (const Show b) const{
        return e_time < b.e_time;
    }
};

Show shows[100];

int main(){
    int n;
    while(scanf("%d", &n) != EOF && n != 0){
        for(int i = 0; i < n; i++){
            scanf("%d %d", &shows[i].s_time, &shows[i].e_time);
        }
        sort(shows, shows + n);
        int cnt = 0, curr_time = 0;
        for(int i = 0; i < n; i++){
            if(curr_time <= shows[i].s_time){
                curr_time = shows[i].e_time;
                cnt++;
            }
        }
        printf("%d\n", cnt);
    }
    return 0;
}