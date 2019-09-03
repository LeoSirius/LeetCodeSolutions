#include<iostream>
#include<map>
using namespace std;

map<string, int> mon_str2num = {
    {"January", 1},
    {"Februray", 2},
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

map<int, string> week_num_to_str = {
    {0, "Sunday"},
    {1, "Monday"},
    {2, "Tuesday"},
    {3, "Wednesday"},
    {4, "Thursday"},
    {5, "Friday"},
    {6, "Saturday"},
};

int
main ()
{
    int year, month, day;
    string m_str;
    while (cin >> day >> m_str >> year) {
        month = mon_str2num[m_str];
        int y, m, d, c;
        if (month == 1 || month == 2) {
            c = (year - 1) / 100;
            y = (year - 1) % 100;
            m = month + 12;
            d = day;
        } else {
            c = year / 100;
            y = year % 100;
            m = month;
            d = day;
        }
        int week = y + y/4 + c/4 - 2*c + 26*(m+1)/10 + d - 1;
        week = (week % 7 + 7) % 7;
        printf("%s\n", week_num_to_str[week].c_str());
    }
}