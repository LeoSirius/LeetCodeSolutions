### 题目描述

一个qq群里有很多师徒关系，如A是B的师父，同时B是A的徒弟。一个师父可能有多个徒弟，一个徒弟也可能有多个师父。输入群里面的所有师徒关系，问群里的师父关系是否合法。一个非法的例子是：A是B的师父，B是C的师父，但是C又是A的师父。

### 输入

The input consists of several test cases. For each case, the first line contains two integers, n(members to be tested) and m(relationships to be tested)(2 <= n, m <= 100). Then m lines follow, each contains a pair of (x, y) which means x is y's master and y is x's prentice. The input is terminated by n = 0, m = 0. To make it simple, we give every one a number(0, 1, 2, ..., n-1). We use their numbers instead of their names.

### 输出

For each test case, print in one line the judgement of the messy relationship. If it is legal, output "YES", otherwise "NO".

### 样例输入

```
3 2
0 1
1 2
2 2
0 1
1 0
6 5
0 1
1 3
3 0
0 2
4 5
6 4
0 1
1 3
0 2
4 5
0 0
```

### 样例输出

```
YES
NO
NO
YES
```