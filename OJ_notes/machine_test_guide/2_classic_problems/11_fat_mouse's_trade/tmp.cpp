#include<iostream>
#include<algorithm>
using namespace std;

struct Room{
    int food;
    int java;
    double ratio;
    bool operator < (const Room & b) const{
        return ratio > b.ratio;
    }
};

int main(){
    int m, n;
    while(scanf("%d%d", &m, &n) != EOF && (m != -1 || n != -1)){
        Room * rooms = new Room[n];
        for(int i = 0; i < n; i++){
            scanf("%d%d", &rooms[i].java, &rooms[i].food);
            rooms[i].ratio = double(rooms[i].java) / rooms[i].food;
        }
        sort(rooms, rooms + n);
        double buy_java_amount = 0;
        for(int i = 0; i < n; i++){
            if(m >= rooms[i].food){
                m -= rooms[i].food;
                buy_java_amount += rooms[i].java;
            }else{
                buy_java_amount += rooms[i].ratio * m;
                break;
            }
        }
        printf("%.3lf\n", buy_java_amount);
        delete [] rooms;
    }
    return 0;
}