### 思路1 转化为与同一时间原点的日期差值

我们把从公元0年1月1日这天到5000年之间所有的日期从0开始算，然后再算两天的日期之查。

有两点注意：

- 我们用一个三位数组保存差值，而年月日是这个差值的数组下标。这种把数据本身同数据的存储地址联系起来的思想就是Hash的基本思想。
- 我们把`buf`数组定义为全局变量而不是放在`main`函数中。若太大的内存定义在函数中，可能栈溢出。凡事需要大量开辟内存空间的情况，我们都定义为全局变量，或用`malloc`等函数动态申请空间。

```cpp
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
```