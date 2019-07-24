#include<iostream>
#define ISLEAP(x) (x % 4 == 0 && x % 100 != 0) || (x % 400 == 0)

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

int hash[5001][13][32];
int abs(int x){return x > 0 ? x : -x;}

int main(){
    Date first_day;
    first_day.d = 1;
    first_day.m = 1;
    first_day.y = 0;
    int count = 0;
    while(first_day.y < 5001){
        hash[first_day.y][first_day.m][first_day.d] = count++;
        first_day.next();
    }

    int y1, m1, d1, y2, m2, d2;
    while(scanf("%4d%2d%2d", &y1, &m1, &d1) != EOF){
        scanf("%4d%2d%2d", &y2, &m2, &d2);
        int diff = hash[y2][m2][d2] - hash[y1][m1][d1];
        printf("%d\n", abs(diff)+1);
    }
    return 0;
}