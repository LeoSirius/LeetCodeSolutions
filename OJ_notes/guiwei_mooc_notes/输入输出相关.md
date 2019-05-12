# 输入输出相关

## 读文件内容作为标准输入

调试程序时手动输入太麻烦，若有测试数据的文件，可以直接用freopen(读作 f re open)。

如文件c:\tmp\test.txt内容：

```c++
1 22 4 7 9 7
```

下面一段代码的运行结果：

```c++
22
```

Code:

```c++
#include<iostream>
using namespace std;
int main(){
    freopen("c:\\tmp\\test.txt", "r", stdin);
    int n, mx = 0;
    while( cin >> n){
        if(n > mx)
            mx = n;
    }
    printf("%d", mx);
}
```

## scanf, printf, cin, cout

- cin、cout速度比scanf、pirntf慢，输入输出大量数据时使用后者
- 一个程序中不要同时使用cin和scanf，cout和printf

### 用scanf读入不同类型的变量

用scanf输入的各项之间用空格分割，但注意若是读入一个字符，输入空格的话会被当成输入的字符

```c++
#include<iostream>
using namespace std;
int main(){
    int n; char c; float f;
    scanf("%d%c%f", &n, &c, &f);
    printf("%d %c %f", n, c, f);
}
```

输入：

```c++
34k 234.45
```

输出：

```c++
34 k 234.449997
```

若输入：

```c++
34_k_456
```

则会输出：

```c++
34  0.000000    //第一个空格给了c，k给了f导致f无效
```

### c++的cin读入

不同于scanf，在读入一个字符时，cin会跳过空格。

下面两种方法，注意scanf用char，cin用int

- 用scanf读入所有输入的字符，包括空格、回车

```c++
#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    char c;
    while(scanf("%c", &C) != EOF)
        printf("%c", c);
    return 0;
}
```

- 用cin读入所有输入的字符，包括空格、回车

```c++
#include<iostream>
using namespace std;
int main(){
    int c;
    //cin.get()返回int类型，即输入字符的ascii码
    while((c = cin.get()) != EOF){
        cout << (char)c;
    }
}
```

### scanf表达式的值

返回值为int，表示成功读入的变量的个数

```c++
int n, m;
printf("%d", scanf("%d%d", &n, &m));

例：
12 56
2

40 a
1        //a没有成功读入，所以只有一个

a 50
0        //第一个就没有成功读入，后面也停止，所以一个
```

scanf也可以返回EOF，windows下按Ctrl+z然后回车，程序结束。linux下则是ctrl+D表示EOF。

敲Ctrl+z，在windos下scanf返回EOF

```c++
//不断输入两个整数，再输出它们的和
int n, m;
while(scanf("%d%d", &n, &m) != EOF)
    printf("%d", n + m);

//另外一种实现方式
int n, m;
while(scanf("%d%d", &n, &m) == 2)
    printf("%d", n + m);
```

### cin表达式的值

cin >> m >> n....    在成功读入所有变量时返回true，否则返回false

Ctrl+z然后回车，读不到东西，cin返回false，跳出循环

```c++
int n, m;
while(cin >> n >> m)
    printf("%d", n+m);
```

## 处理无结束标记的OJ题目

输入若干个（不知道多少个）正整数，输出其中的最大值

Sample Input:

```c++
2 3 4 5 6 787 54532 12
```

Sample Output:

```c++
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