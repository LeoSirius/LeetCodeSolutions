### 思路1 转化为与同一时间原点的日期差值

我们把输入的两天与00000101这天的日期之差算出来，然后再算两天的日期之查。

有两点注意：

- 我们用一个三位数组保存差值，而年月日是这个差值的数组下标。这种把数据本身同数据的存储地址联系起来的思想就是Hash的基本思想。
- 我们把`buf`数组定义为全局变量而不是放在`main`函数中。若太大的内存定义在函数中，可能栈溢出。凡事需要大量开辟内存空间的情况，我们都定义为全局变量，或用`malloc`等函数动态申请空间。

```cpp
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
```