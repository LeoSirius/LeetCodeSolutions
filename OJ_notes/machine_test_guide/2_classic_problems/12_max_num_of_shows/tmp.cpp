#include<iostream>
#include<algorithm>
using namespace std;

struct Program{
    int s_time;
    int e_time;
    bool operator < (const Program B)const{
        return e_time < B.e_time;
    }
};

int main(){
    int n;
    while(scanf("%d", &n) != EOF && n != 0){
        Program * programs = new Program[n];
        for(int i = 0; i < n; i++){
            scanf("%d%d", &programs[i].s_time, &programs[i].e_time);
        }
        sort(programs, programs + n);
        int cur_time = 0;
        int cnt = 0;
        for(int i = 0; i < n; i++){
            if(cur_time <= programs[i].s_time){
                cur_time = programs[i].e_time;
                cnt++;
            }
        }
        printf("%d\n", cnt);
        delete [] programs;
    }
    return 0;
}