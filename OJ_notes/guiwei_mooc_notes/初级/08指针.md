# 指针

## 指针的相互赋值

不同类型的指针，如果不经过强制类型转换，不能直接相互赋值

## 指针的运算

1. 两个同类型的指针变量，可以比较大小（比较的就是地址的大小）
2. 两个同类型的指针变量，可以相减`p1 - p2 = (地址p1 - 地址p2) / sizoef(T)`，表示p1和p2之间还能存放多少个T类型的变量。
3. 指针变量可以加减一个整数，结果是指针
4. 指针可以用下标运算符`[]`进行运算`p[n]`等价于`*(p+n)`

## 空指针

地址0不能访问，指向地址0的指针就是空指针，`NULL`（就是整数0）可以对任何类型的指针赋值，值为`NULL`的指针就是空指针。

## 指针和数组

数组名就是一个指针常量，指向数组的起始地址。作为函数的型参时，`T *p`和`T p[]`等价，也就是说，传递数组会被函数当成指针。

例子：颠倒一个数组

```c++
#include<iostream>
using namespace std;
void Reverse(int *p, int size){
    for(int i = 0; i < size / 2; i++){
        int tmp = p[i];
        p[i] = p[size - 1 - i];
        p[size - 1 - i] = tmp;
    }
}

int main(){
    int a[5] = {1, 2, 3, 4, 5};
    Reverse(a, sizeof(a) / sizeof(int));
    for(int i = 0; i < 5; i++){
        cout << *(a + i) << ", ";
    }
    return 0;
}
```

## 指针和二维数组

如果定义二维数组`T a[M][N]`，则：

- `a[i]`是一个一位数组
- `a[i]`的类型是`T *`
- `sizeof(a[i]) = sizeof(T) * N`
- `a[i]`指向的地址：数组a的起始地址 + `sizeof(T) * N * i`

## 指向指针的指针

看一个例子：

```c++
#include<iostream>
using namespace std;
int main(){
    int **pp;
    int *p;
    int n = 1234;
    p = &n;     // p指向n
    pp = &p;    // pp指向p
    cout << *(*pp) << endl; // 输出1234
    return 0;
}
```

## 指针和字符串

- 字符数组名的类型是`char *`
- 字符串常量的类型是`char *`

如
```c++
char *p = "Please input your name:\n";
cout << p; // 用printf(p);效果一样
```

## void指针

可以用任何类型的指针对void指针进行赋值。

### memset

`void *memset(void *dest, int ch, int n)`
将从dest开始的n个字节，都设置成ch的第一个字节的内容。

例如把整形数组a中的所有元素都变成0，可以用
`memset(a, 0, sizeof(a));`

### memcpy

`void *memcpy(void *dest, void *src, int n)`
将从src开始的n个字节拷贝到dest。

例如把a1的前10个元素拷贝到a2中
`memcpy(a2, a1, 10 * sizeof(int));`

memcpy的一种实现

```c++
void *MyMemcpy(void *dest, const void *src, int n){
    char *pDest = (char *)dest;
    char *pSrc = (char *)src;
    for(int i = 0; i < n; ++i)
        *(pDest + i) = *(pSrc + i);
    return dest;
}
```

## 函数指针

程序运行期间，每个函数都会占用一段连续的内存空间。函数名就是这段内存空间的起始地址。用一个指针变量指向函数的起始地址，然后通过指针变量就可以调用函数。这个指针变量就是函数指针。

一个例子

```c++
#include<stdio.h>
void PrintMin(int a, int b){
    if(a < b)
        printf("%d", a);
    else
        printf("%d", b);
}

int main(){
    void(*pf)(int, int);
    int x = 4, y = 5;
    pf = PrintMin;
    pf(x, y);
    return 0;
}
```

在来看看快速排序的库函数`qsort`
`void qsort(void *base, int nelem, unsigned int width, int(*pfCompare)(const void*, const void*));`

参数说明：

- base：待排序数组的起始地址
- nelem：待排序数组的元素个数
- width：数组中每个元素的大小（单位是字节）
- pfCompare：比较函数的地址

比较函数:
`int FuncName(const void *e1, const void *e2);`

比较函数的编写规则：

- 如果e1应该在e2前面，则函数返回负整数
- 如果e1和e2那个排在前面都行，则返回0
- 如果e1应该排在e2后面，则函数应该返回正整数

一个例子，按照个位数的大小排序

```c++
#include<stdio.h>
#include<stdlib.h>

int MyCompare(const void *e1, const void *e2){
    unsigned int *p1, *p2;
    p1 = (unsigned int*)e1;
    p2 = (unsigned int*)e2;
    return (*p1 % 10) - (*p2 % 10);
}

int main(){
    unsigned int an[5] = {8, 123, 11, 10, 4};
    qsort(an, 5, sizeof(unsigned int), MyCompare);
    for(int i = 0; i < 5; i++)
        printf("%d ", an[i]);    //输出 10 11 123 4 8
    return 0;
}
```