### 题目描述

把一个个大小差一圈的框叠上去，使得从上往下看时，边框花色交错。

### 输入

输入是一个三元组，分别是，外框尺寸n（0 < n < 80，且为奇整数），中心花色字符，外框花色字符。后二者都为ascii可见字符。

### 输出

输出叠在一起的框图案。中心花色与外框花色字符从内层起交错相叠。多框相叠时，最外框的角总是被打磨掉。叠框与叠框之间应有一行间隔。

### 样例输入

```
11 B A
5 @ W
```

### 样例输出

```
 AAAAAAAAA 
ABBBBBBBBBA
ABAAAAAAABA
ABABBBBBABA
ABABAAABABA
ABABABABABA
ABABAAABABA
ABABBBBBABA
ABAAAAAAABA
ABBBBBBBBBA
 AAAAAAAAA 

 @@@ 
@WWW@
@W@W@
@WWW@
 @@@ 
```