#include<stdio.h>
#define ISLEAP(x) (x % 100 != 0 && x % 4 == 0) || x % 400 == 0

int dayOfMonth[13][2] = {
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
    int Day, Month, Year;
    void NextDay(){
        Day++;
        if(Day > dayOfMonth[Month][ISLEAP(Year)]){
            Day = 1;
            Month++;
            if(Month > 12){
                Month = 1;
                Year++;
            }
        }
    }
};

int buf[5001][13][32];
int Abs(int x){
    return x < 0 ? -x : x;
}

int main(){
    Date tmp;
    int cnt = 0;
    tmp.Day = 1;
    tmp.Month = 1;
    tmp.Year = 0;
    while(tmp.Year != 5001){
        buf[tmp.Year][tmp.Month][tmp.Day] = cnt;   //将该天与00000101之间的差值保存起来，这里的差值是正常意义的差值
        tmp.NextDay();
        cnt++;
    }
    int d1, m1, y1, d2, m2, y2;
    while(scanf("%4d%2d%2d", &y1, &m1, &d1) != EOF){
        scanf("%4d%2d%2d", &y2, &m2, &d2);
        printf("%d\n", Abs(buf[y2][m2][d2] - buf[y1][m1][d1]) + 1);
    }
    return 0;
}