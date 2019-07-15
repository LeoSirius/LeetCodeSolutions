#include<iostream>
#include<algorithm>
using namespace std;

struct Room{
    int food;
    int javabean;
    double ratio;
    bool operator < (const Room &b) const {
        return ratio > b.ratio;
    }
};

int main(){
    int m, n;
    while(scanf("%d %d", &m, &n) != EOF && !(m == -1 && n == -1)){
        Room *rooms = new Room[n];
        for(int i = 0; i < n; ++i){
            scanf("%d %d", &rooms[i].javabean, &rooms[i].food);
            rooms[i].ratio = double(rooms[i].javabean) / rooms[i].food;
        }
        sort(rooms, rooms + n);
        double total_javabean = 0;
        for(int i = 0; i < n && m; i++){
            if(m > rooms[i].food){
                total_javabean += rooms[i].javabean;
                m -= rooms[i].food;
            }else{
                total_javabean += m * rooms[i].ratio;
                m = 0;
            }
        }
        printf("%.3f\n", total_javabean);
    }
    return 0;
}