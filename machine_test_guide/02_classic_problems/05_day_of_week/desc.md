### 题目描述

We now use the Gregorian style of dating in Russia. The leap years are years with number divisible by 4 but not divisivle by 100, or divisible by 400. For example, years 2004, 2180, and 2400 are leap. Years 2181, 2300 are not heap.

Your task is to write a program which will compute the day of the weeek correspoding to a given data in the nearest past or in the future using today's agreement about dating.

### 输入

There is one single line contains the day number d, month name M and year number y( 1000 <= y <= 3000). The month name is the corresponding English name starting from the capital letter.

### 输出

Output a single line with the English name of the day of week corresponding to the date, starting from the capital letter. All other letters must be in lower case.

### 样例输入

```
4 September 2019
1 October 2019
```

### 样例输出

```
Tuesday
Sunday
```