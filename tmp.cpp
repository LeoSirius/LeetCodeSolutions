#include<iostream>
#include<algorithm>
using namespace std;

struct Room{
    double javabean;
    double food;
    double ratio;
    bool operator < (const Room &b)const{
        return ratio > b.ratio;
    }
};

int main(){
    int m, n;
    while(scanf("%d %d", &m, &n) == 2 && !(m == -1 && n == -1)){
        Room *rooms = new Room[n];
        for(int i = 0; i < n; i++){
            scanf("%lf %lf", &rooms[i].javabean, &rooms[i].food);
            rooms[i].ratio = rooms[i].javabean / rooms[i].food;
        }
        sort(rooms, rooms+n);
        double javabean_buy = 0;
        for(int i = 0; i < n && m > 0; ++i){
            if(m >= rooms[i].food){
                javabean_buy += rooms[i].javabean;
                m -= rooms[i].food;
            }else{
                javabean_buy += rooms[i].ratio * m;
                m = 0;
            }
        }
        printf("%.3f\n", javabean_buy);
        delete [] rooms;
    }
}