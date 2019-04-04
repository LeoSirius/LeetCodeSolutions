# 例4_Day_of_Week

**题目描述：**

```
Your task is to write a program which will compute the day of week 
corresponding to a given data in the neareast past or in the future using 
today's agreement about dating.
```

**输入：**

```
There is one single line contains the day number d, month name M and year number y
(1000 <= y <= 3000). The month name is the corresponding English name
starting from the capital letter.
```

**输出：**

```
as sample.
```

**输入样例：**

```
9 October 2001
14 October 2001
```

**输出样例：**

```
Tuesday
Sunday
```



**思路：**

```
利用例3的思路，我们知道今天是星期几，今天和输入的天数差了几天，再%7便可得到
C99 规定，如果 % 左边的操作数是正数，则模除的结果为正数或零；
如果 % 左边的操作数是负数，则模除的结果为负数或零。
(days % 7 + 7) % 7   保证的得到的是个正数
```



**代码：**

```c++
#include<iostream>
#include<string>
#define ISLEAP(x) x % 100 != 0  && x % 4 == 0 || x % 400 == 0

int dayOfMonth[13][2] = {
	0,0,
	31,31,
	28,29,		//闰年2月多一天
	31,31,
	30,30,
	31,31,
	30,30,
	31,31,
	31,31,
	30,30,
	31,31,
	30,30,
	31,31
};

struct Date {
	int day;
	int month;
	int year;
	void nextDay() {
		day++;
		if (day > dayOfMonth[month][ISLEAP(year)]) {
			day = 1;
			month++;
			if (month > 12) {
				month = 1;
				year++;
			}
		}
	}
};

int buf[3001][13][32];
char monthName[13][20] = {
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
	"December"
};
char weekName[7][20] = {
	"Sunday",
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday"
};

int main() {
	Date tmp;
	int cnt = 0;
	tmp.day = 1;
	tmp.month = 1;
	tmp.year = 0;
	//将该日与0年1月1日之间的差保存起来
	while (tmp.year != 3001) {
		buf[tmp.year][tmp.month][tmp.day] = cnt;
		tmp.nextDay();
		cnt++;
	}
	int d, m, y;
	char s[20];
	while (scanf("%d %s %d", &d, s, &y) != EOF) {
		for (m = 1; m <= 12; m++)
			if (strcmp(s, monthName[m]) == 0)
				break;
		int days = buf[y][m][d] - buf[2019][1][21];		//2019 1 21  已知的一个星期一, 注意days可能为负
		days += 1;
		puts(weekName[(days % 7 + 7) % 7]);
	}
	return 0;
}
```

