# Introduction

初级从第七周（字符串）开始做笔记。





tips:

调试程序时手动输入太麻烦，若有测试数据的文件，可以直接用freopen(读作 f re open)。

例：

文件c:\tmp\test.txt内容：

```
1 22 4 7 9 7
```

下面一段代码的运行结果：

```
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

