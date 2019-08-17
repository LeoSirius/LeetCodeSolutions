### 题目描述

In an episode of the Dick Van Dyke show, little Richie connects the freckles on his Dad's back to form a picture of the Liberty Bell. Alas, one of the freckles turns out to be a scar, so his Richie's engagement falls through. Consider Dick's back to be a plane with freckles at various (x, y) locations. Your job is to tell Richie how to connect the dots so as to minimize the amount of ink used. Richie connects the dots by drawing straight lines between pairs, possibly lifting the pen between lines. When Richie is done there must be a sequence of connected lines from any freckle to any other freckle.

### 输入

The first line contains 0 <= n <= 100, the number of freckles on Dick's back. For each freckle, a line follows; each following line contains two real nubmers indicating the (x, y) coordinates of the freckles.

### 输出

Your program prints a single real number to two decimal places: the minimum total length of ink lines that can connect all the freckls.

### 样例输入

```
3
1.0 1.0
2.0 2.0
2.0 4.0
```

### 样例输出

```
3.41
```