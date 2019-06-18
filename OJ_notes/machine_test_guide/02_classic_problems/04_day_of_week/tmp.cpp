#include<iostream>
#include<string>
#define ISLEAP(x) (x % 4 == 0 && x % 100 != 0) || x % 400 == 0
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

char month_mapping[13][20] = {
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
};

char week_mapping[7][20] = {
    "Sunday",
    "Monday",
    "Teusday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
};

struct Date{
    int d, m, y;
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

int cnt_bfr[3001][13][32];
int abs(int x){
    return x > 0 ? x : -x;
}

int main(){
    Date tmp;
    tmp.y = 0;
    tmp.d = tmp.m = 1;
    int cnt = 0;
    while(tmp.y < 3001){
        cnt_bfr[tmp.y][tmp.m][tmp.d] = cnt;
        cnt++;
        tmp.next();
    }
    int d, y, m;
    char m_str[20];
    while(scanf("%d%s%d", &d, m_str, &y) != EOF){
        for(int i = 1; i <= 12; i++){
            if(strcmp(m_str, month_mapping[i]) == 0){
                m = i;
                break;
            }
        }
        int diff = (cnt_bfr[y][m][d] - cnt_bfr[2019][6][3]) + 1;
        printf("%s\n", week_mapping[(diff % 7 + 7) % 7]);
    }

}