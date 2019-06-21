##### 思路1 利用日期差值来求

先利用例3的思路，把所有的日期差值保存在一个三位数组中。星期是以7天为循环的，那么我们只要知道：1离今天最近的星期日是哪天；2那天和所给定的那天相隔几天。利用其对7的余数，就可以求出答案。

注意最后求日期差值的时候谁减谁的顺序不能反，必须是求的那天减基准日期。

```cpp
#include<iostream>
#include<string>
#include<map>
using namespace std;
#define ISLEAP(x) (x % 4 == 0 && x % 100 != 0) || x % 400 == 0

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
    void next_day(){
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

map<string, int> month_str_to_num;
map<int, string> week_num_to_str;

int hashing[3001][13][32];     //月日都从1开始
Date tmp_date;

void init(){
    int cnt = 0;
    tmp_date.y = 0, tmp_date.m = 1, tmp_date.d = 1;
    while(tmp_date.y < 3001){
        hashing[tmp_date.y][tmp_date.m][tmp_date.d] = cnt;
        cnt++;
        tmp_date.next_day();
    }
    month_str_to_num.insert(pair<string, int>("January", 1));
    month_str_to_num.insert(pair<string, int>("Februray", 2));
    month_str_to_num.insert(pair<string, int>("March", 3));
    month_str_to_num.insert(pair<string, int>("April", 4));
    month_str_to_num.insert(pair<string, int>("May", 5));
    month_str_to_num.insert(pair<string, int>("June", 6));
    month_str_to_num.insert(pair<string, int>("July", 7));
    month_str_to_num.insert(pair<string, int>("August", 8));
    month_str_to_num.insert(pair<string, int>("September", 9));
    month_str_to_num.insert(pair<string, int>("October", 10));
    month_str_to_num.insert(pair<string, int>("November", 11));
    month_str_to_num.insert(pair<string, int>("December", 12));
    week_num_to_str.insert(pair<int, string>(0, "Sunday"));
    week_num_to_str.insert(pair<int, string>(1, "Monday"));
    week_num_to_str.insert(pair<int, string>(2, "Tuesday"));
    week_num_to_str.insert(pair<int, string>(3, "Wednesday"));
    week_num_to_str.insert(pair<int, string>(4, "Thursday"));
    week_num_to_str.insert(pair<int, string>(5, "Friday"));
    week_num_to_str.insert(pair<int, string>(6, "Saturday"));
}

int main(){
    init();
    int y, m, d;
    string m_str;
    while(cin >> d >> m_str >> y){
        m = month_str_to_num[m_str];
        int diff = hashing[y][m][d] - hashing[2019][6][23]; // 和已知的一个星期日之间的日期差
        //这样不是简单的取绝对值，如-1经过下边的运算会变成6，所以上面减的顺序也不能变
        cout << week_num_to_str[(diff % 7 + 7) % 7] << endl;
    }
}
```