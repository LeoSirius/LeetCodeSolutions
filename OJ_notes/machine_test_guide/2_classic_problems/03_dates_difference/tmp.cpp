#include<iostream>
#define ISLEAP(x) (x % 4 == 0 && x % 100 != 0)
using namespace std;

int day_of_month[13][2] = {
    0,0,
    31,31,
    28,29,
    31,31,
    30,30,
    31,31,
    30,30,
    31,31,
    31,31,
    30,30,
    31,31,
    30,30,
    31,31,
};

struct Date{
    int y, m, d;
    void next(){
        d++;
        if(d > day_of_month[m][ISLEAP(y)]){
            d = 1;
            m++;
            if(m > 12){
                m = 1;
                y++;
            }
        }
    }
};

int cnt_bfr[5001][13][32];
int abs(int x){
    return x > 0 ? x : -x;
}

int main(){
    Date tmp_day;
    tmp_day.y = 0;
    tmp_day.m = tmp_day.d = 1;
    int cnt = 0;
    while(tmp_day.y < 5001){
        cnt_bfr[tmp_day.y][tmp_day.m][tmp_day.d] = cnt;
        cnt++;
        tmp_day.next();
    }
    int d1, m1, y1, d2, m2, y2;
    while(scanf("%4d%2d%2d", &y1, &m1, &d1) == 3){
        scanf("%4d%2d%2d", &y2, &m2, &d2);
        printf("%d\n", abs(cnt_bfr[y2][m2][d2] - cnt_bfr[y1][m1][d1]) + 1);
    }
    return 0;
}
