#include<iostream>
#include<map>
using namespace std;

map<string, int> monthstr2int = {
    {"January", 1},
    {"February", 2},
    {"March", 3},
    {"April", 4},
    {"May", 5},
    {"June", 6},
    {"July", 7},
    {"August", 8},
    {"September", 9},
    {"October", 10},
    {"November", 11},
    {"December", 12},
};

int main()
{
    int day, month, year;
    string mon_str;
    while (cin >> day >> mon_str >> year) {
        month = monthstr2int[mon_str];
        int c = year / 100;
        int y = year % 100;
        int m;
        if (month >= 3) {
            m = month;
        } else {
            m = month + 12;
            y -= 1;
        }
        int w = y + y / 4 + c / 4 - 2 * c + (26 * (m + 1)) / 10 + day - 1;
        printf("%d\n", w % 7);
    }
    return 0;
}