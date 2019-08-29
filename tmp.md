### 题目描述

对输入的n个数进行排序并输出。

### 输入

输入的第一行包括一个整数n（1 <= n <= 100）。接下来的一行包括n个整数。

### 输出

可能有多组测试数据，对每组测试数据，将排序后的n个整数输出，每个数后面都有一个空格。每个测试用例的结果占一行。

### 样例输入

```
4
1 4 3 2
```

### 样例输出

```
1 2 3 4 
```

### 思路1 用内置sort排序

内置`sort`是用的快排实现，n*logn的复杂度

```cpp
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        vector<int> input_array;
        int tmp;
        for(int i = 0; i < n; i++){
            scanf("%d", &tmp);
            input_array.push_back(tmp);
        }
        sort(input_array.begin(), input_array.end());

        // no space after laster number, so treat it alone
        for(int i = 0; i < input_array.size() - 1; i++){
            printf("%d ", input_array[i]);
        }
        printf("%d", input_array[input_array.size()-1]);
        printf("\n");
    }
    return 0;
}
```