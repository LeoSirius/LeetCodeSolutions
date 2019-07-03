## FatMouse' Trade

### 题目描述

FatMouse prepared M pounds of cat food, ready to trade with the cats guarding the warehouse containing her favorite food, JavaBean.
The warehouse has N rooms. The i-th room contains J[i] pounds of JavaBeans and requires F[i] pounds of cat food. FatMouse does not have to trade for all the JavaBeans in the room, instead, she may get J[i] * a% pounds of JavaBeans if she pays F[i] * a% pounds of cat food. Here 'a' is a real number. Now she is assigning this homework to you: tell her the maximum amount of JavaBean she can obtain.

### 输入

The input consists of multiple test cases. Each test case begins with a line containing two non-negative integers M and N, The N lines follow, each contians two non-negative integers J[i] and F[i] respectively. The last test case is followd by two -1s. All integers are not greater than 1000.

### 输出

For each test case, print in a single line a real number accurate up to 3 decimal places, which is the maximum amount of JavaBeans that FatMouse can obtain.

### 样例输入

```
5 3
7 2
4 3
5 2
20 3
25 18
24 15
15 10
-1 -1
```

### 样例输出

```
13.333
31.500
```