# OOP basics

## 类和对象的基本概念和用法

对象占用的内存空间大小：等于所有成员变量的大小只和。注意成员函数只有一份，不会放在对象中。

和结构变量一样，对象之间可以用 = 进行赋值，但是不能直接用“== != > < >= <=”进行比较，除非对他们进行了重载。

### 类成员的可访问范围

缺省类型是私有。

在类的成员函数的内部，可以访问：

- 当前对象的全部属性，函数
- 同类其他对象的全部属性，函数

## 构造函数

对象的存储空间不是构造函数分配的。构造函数只是在已经分配好的存储空间中去做一些初始化的工作。

构造函数在数组中的使用：

```cpp
class Test{
    public:
        Test(int n){}           // 1
        Test(int n, int m) {}   // 2
        Test(){}                // 3
};
Test array1[3] = {1, Test(1,2)};            // 三个元素分别用1 2 3 初始化
Test array2[3] = {Test(2,3), Test(1,2), 1}; // 三个元素分别用2 2 1初始化
Test *pArray[3] = {new Test(4), new Test(1,2)}
```

注意`pArray`是指针数组，需要用new创建对数组元素（即指针）所指向的对象。这里只创建了两个对象。pArray[2]没有被初始化。

## 复制构造函数

- 只有一个参数，即对同类对象的引用
- 形如：`X::X(X &)`或`X::X(const X &)`，后者能以常量对象最为参数
- 如果没有复制构造函数，编译器会自动生成一个

复制构造函数起作用的三种情况

1 当用一个对象去初始化同类的另一个对象

```cpp
Complex c2(c1);
Complex c2 = c1;    // 同上面的语句效果一样，注意这是初始化语句，不是赋值语句！！！！
```

注意这两种情况调用的不是复制构造函数

```cpp
Complex c1 = Complex(1,2);
Complex c2(Complex(1,2));
```

2 函数的参数是类的对象。调用函数时，复制构造函数被调用。
3 函数的返回值是一个对象，则函数返回时，复制构造函数被调用。

**注意：对象间赋值不会调用复制构造函数**

```cpp
class CMyclass{
public:
    int n;
    CMyclass(){};
    CMyclass(CMyclass & c){
        n = 2 * c.n;
    }
};
int main(){
    CMyclass c1, c2;
    c1.n = 5;
    c2 = c1;               // 注意这是赋值语句，不是初始化，复制构造函数不会被调用
    CMyclass c3 = c1;      // 这是初始化，复制构造函数会被调用
    cout << "c2.n" << c2.n << endl;
    cout << "c3.n" << c3.n << endl;
    return 0;
}
```

输出

```cpp
c2.n = 5
c3.n = 10
```

常量引用参数的使用：

```cpp
void fun(CMyclass obj_){
    cout << "fun" << endl;
}
```

- 这样的函数，调用时形参会引发复制构造函数调用，开销较大
- 可以考虑使用`CMyclass &`引用类型作为参数。引用是原对象的一个别名
- 如果希望原对象的值不被改变，可以加上`const`关键字

## 类型转换构造函数

什么是类型转换构造函数：

- 定义转换构造函数的目的是实现类型的自动转换。
- 只有一个参数，而且参数不是复制构造函数的构造函数，一般就可以看作是转换构造函数。
- 当需要的时候，编译系统会自动调用转换构造函数，建立一个无名的临时对象（或临时变量）。

```cpp
class Complex{
public:
    double real, imag;
    // 类型转换构造函数
    Complex(int i){         
        cout << "IntConstructor called" << endl;
        real = i; imag = 0;
    }
    Complex(double r, double i){real = r; imag = i;}
}

int main(){
    Complex c1(7, 8);
    Complex c2 = 12;    // 调用类型转换构造函数
    c1 = 9;    // 9被自动转换成一个临时Complex对象，然后赋值给c1
    cout << c1.real << ", " << c1.imag << endl;
    return 0l
}
```

## 析构函数

- 名字与类名相同，在前面加~， 没有参数和返回值，一个类最多只能有一个析构函数。
- 在对象消亡的时候自动被调用。可定义析构函数来在对象消亡前做一些善后工作，比如释放分配的空间等。
- 如果定义类时没有写析构函数，编译器会自动生成缺省的析构函数，其什么也不做。

>注意同构造函数，析构函数本身也不负责回收空间，它只是在操作系统回收空间之前做一些工作。

一个析构函数的例子：在构造函数中动态分配存储空间，在析构函数中`delete`掉

```cpp
class String{
private:
    char *p;

public:
    String(){
        p = new char[10];
    }
    ~String();
}

String::~String(){
    delete [] p;
}
```

对象数组生命周期结束时，对象数组的每个元素的析构函数都会被调用：

```cpp
class Ctets{
public:
    ~Ctets(){
        cout << "destructor called" << endl;
    }
};

int main(){
    Ctets array[2];
    cout << "End Main" << endl;
    return 0;
}
```

上面的程序会输出：

```
End Main
destructor called
destructor called
```

对于`new`出来的对象，一定要`delete`，不然不会消亡。

```cpp
pTest = new Ctest[3];   // 构造函数被调用3次
delete [] pTest;        // 析构函数被调用3次
```

我们再来看一个析构函数调用的例子：

```cpp
class CMyClass{
public:
    ~CMyClass(){
        cout << "desctructor" << endl;
    }
};

CMyClass obj;

CMyClass fun(CMyClass sobj){  // 参数对象的消亡，第一次调用
    return sobj;
}

int main(){
    // 函数调用的返回值（临时对象）消亡，第二次调用
    // 临时对象一般在其所在的语句执行完后消亡
    obj = fun(obj);
    return 0;
}
// 整个程序结束后全局的obj消亡，第三次调用
```

输出
```
destructor
destructor
destructor
```

## 构造函数和析构函数调用时机

我们再来看一个复杂一点的例子

```cpp
#include<iostream>
using namespace std;

class Demo{
    int id;

public:
    Demo(int i){
        id = i;
        cout << "id = " << id << " constructed" << endl;
    }
    ~Demo(){
        cout << "id = " << id << " destructed" << endl;
    }
};

Demo d1(1);

void fun(){
    static Demo d2(2);
    Demo d3(3);
    cout << "fun" << endl;
}

int main(){
    Demo d4(4);
    d4 = 6;
    cout << "main" << endl;
    {
        Demo d5(5);
    }
    fun();
    cout << "main ends" << endl;
    return 0;
}
```

输出

```
id = 1 constructed
id = 4 constructed
id = 6 constructed  // 转换构造函数会生成一个临时对象，赋值给d4，然后消亡
id = 6 destructed
main
id = 5 constructed
id = 5 destructed
id = 2 constructed
id = 3 constructed
fun
id = 3 destructed
main ends
id = 6 destructed   // d4的值被改成了6
id = 2 destructed   // 静态变量一般先构造的后析构，所以这里d1在d2后面
id = 1 destructed
```