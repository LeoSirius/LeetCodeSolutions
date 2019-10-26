#include<iostream>
using namespace std;

#define IS_LEAP(x) ((x % 4 == 0 && x % 100 != 0) || (x % 400 == 0))

int get_max_day_in_month(int y, int m)
{
    switch (m) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            return 31;
        case 4:
        case 6:
        case 9:
        case 11:
            return 30;
        case 2:
            return IS_LEAP(y) ? 29 : 28;
    }
}

struct Date
{
    Date(int y, int m, int d): y(y), m(m), d(d) {};
    int y, m, d;
    void next()
    {
        d++;
        if (d > get_max_day_in_month(y, m)) {
            d = 1;
            m++;
            if (m > 12) {
                m = 1;
                y++;
            }
        }
    }
};

int buf[5001][13][32];

void init()
{
    Date date(0, 0, 0);
    int count = 0;
    while (date.y < 5001) {
        buf[date.y][date.m][date.d] = count;
        count++;
        date.next();
    }
}

int main()
{
    init();
    int y1, m1, d1, y2, m2, d2;
    while (scanf("%4d%2d%2d", &y1, &m1, &d1) != EOF) {
        scanf("%4d%2d%2d", &y2, &m2, &d2);
        int diff = abs(buf[y1][m1][d1] - buf[y2][m2][d2]) + 1;
        printf("%d\n", diff);
    }
    return 0;
}