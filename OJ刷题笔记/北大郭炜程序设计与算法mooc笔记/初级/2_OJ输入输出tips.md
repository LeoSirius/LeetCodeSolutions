# scanf表达式的值

返回值为int，表示成功读入的变量的个数

```c++
int n, m;
printf("%d", scanf("%d%d", &n, &m));

例：
12 56
2
    
40 a
1		//a没有成功读入，所以只有一个

a 50
0		//第一个就没有成功读入，后面也停止，所以一个
```



scanf也可以返回EOF，windows下按Ctrl+z然后回车，程序结束

敲Ctrl+z，在windos下scanf返回EOF

```c++
//不断输入两个整数，再输出它们的和
int n, m;
while(scanf("%d%d", &n, &m) != EOF)
    printf("%d", n + m);

//另外一种实现方式
int n, m;
while(scanf("%d%d", &n, &m) == 2)
    printf("%d", n+m);
```



# cin表达式的值

cin >> m >> n....    在成功读入所有变量时返回true，否则返回false

Ctrl+z然后回车，读不到东西，cin返回false，跳出循环

```c++
int n, m;
while(cin >> n >> m)
    printf("%d", n+m);
```



# 处理无结束标记的OJ题目

输入若干个（不知道多少个）正整数，输出其中的最大值

Sample Input:

```
2 3 4 5 6 787 54532 12
```

Sample Output:

```
54532
```

Code:

```c++
#include<iostream>
using namespace std;
int main(){
	int n mx = 0;
    //用cin则是: while(cin >> n)
    while(scanf("%d", &n) != EOF){
        if(n > mx)
            mx = 0;
    }
    printf("%d", mx);
    return 0;
}
```

