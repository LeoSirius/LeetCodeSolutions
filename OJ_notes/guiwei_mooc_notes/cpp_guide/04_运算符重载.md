# 运算符重载

## 运算符重载的基本概念

运算符重载的需求：cpp预定义的运算符，只能用于基本数据类型的运算，不能用于对象之间。

运算符重载的实质是函数重载：

- 把包含运算符的表达式转换成对运算符函数的调用。
- 把运算符的操作数转换成运算符函数的参数

运算符重载的形式：

```
返回值类型 operator 运算符(形参表){
    ...
}
```

一个例子：

```cpp
class Complex{
public:
    double real, imag;
    Complex(double r = 0.0, double i = 0.0):real(r), imag(i){}
    Complex operator-(const Complex &c);
};

// 重载为普通函数，参数个数为运算符数目
Complex operator+(const Complex &a, const Complex &b){
    return Complex(a.real+b.real, a.imag+b.imag);      // 返回一个临时对象
}

// 重载为成员函数，参数个数为运算符数目减一
Complex Complex::operator-(const Complex &c){
    return Complex(real-c.real, imag-c.imag);       // 返回一个临时对象
}
```

## 赋值运算符的重载

重载赋值运算符的需求：赋值运算符两边的类型可以不匹配。（如把int类型的变量赋值给一个Complex对象）

> 赋值运算符只能重载为成员函数

一个`String`类的例子

```cpp
class String{
private:
    char *str;

public:
    // 构造函数，new一个字符，并让str指向那个字符，且初始化为0
    String():str(new char[1]){str[0] = 0;}
    const char *c_str(){return str;}
    String &operator=(const char *s);
    ~String(){delete [] str;}
};

String &String::operator=(const char *s){
    // 重载，使得obj = ”hello“能够成立
    delete [] str;
    str = new char[strlen(s)+1];
    strcpy(str, s);
    return *this;       // this是指向当前对象的指针， *this就是当前对象。
}

int main(){
    // 注意 String s = "Good Luck"; 这样写会报错, 因为这是初始化语句，而我们重载的是赋值运算符
    String s;
    s = "Good Luck";
    cout << s.c_str() << endl;
    s = "new Luck";
    cout << s.c_str() << endl;
    return 0;
}
```

输出：

```
Good Luck
new Luck
```

## 浅拷贝与深拷贝

上面那个`String`类的例子只能实现浅拷贝，因为对象之间的赋值运算符并没有重载，如果直接赋值，会进行对象复制，会把两个对象中的值变成一样，两个对象的str会指向同一个地方。且会产生内存垃圾（`"aaaa"`并没有被析构函数执行，内存也没有回收），且消亡时，`"bbbb"`那片空间会被`delete`两次，会出错。

```cpp
String s1, s2;
s1 = "aaaa";
s2 = "bbbb";
s1 = s2;
```

为了使对象之间能够赋值，要在`class String`中加成员函数：

```cpp
String &operator=(const String &s){
    delete [] str;
    str = new char[strlen(s.str)+1];
    strcpy(str, s.str);
    return *this;       // this是指向当前对象的指针， *this就是当前对象。
}
```

上面其实还有一个问题，如果写`s = s`，str在一开始就会被delete，下面执行变会出错。改进方法：

```cpp
String &operator=(const String &s){
    // 如果this指针和传进来的对象地址相同，则直接返回。
    if(this == &s)
        return *this;
    delete [] str;
    str = new char[strlen(s.str)+1];
    strcpy(str, s.str);
    return *this;       // this是指向当前对象的指针， *this就是当前对象。
}
```

最后，为什么要返回`String &`？如果我们只写一个赋值，其实返回值是没有被接收的，之所以返回`String &`是为了让`a = b = c`这样的写法不会报错。

其实上面的String类还有一个问题，除了赋值语句外，还有两种情况会调用复制构造函数，这时两个对象会指向同一片区域。为了避免这样的问题，我们还要重写复制构造函数：

```cpp
String(String &s){
    str = new char[strlen(s.str)+1];
    strcpy(str, s.str);
}
```

总结一下这个`String`类，一共重写了三个地方：

- 对`char *s`的重载，使之能接受`char *s`变量的赋值
- 对同类对象的重载，使之能接受同类对象的赋值
- 对复制构造函数的重载，使其被调用时`str`不会指向同一内存。

## 重载运算符为友元函数

- 一般情况下，将运算符重载为成员函数，是较好的选择
- 但有时，重载为成员函数不能满足使用要求，重载为普通函数，又不能访问类的私有成员，所以需要重载为友元函数

```cpp
class Complex{
    double real, imag;

public:
    Complex(double r, double i):real(r), imag(i){};
    Complex operator+(double r);
};

// 重载为成员函数，只能解释c+5， 5+c会编译出错
Complex Complex::operator+(double r){
    return Complex(real+r, imag);
}
```

为了使5+c也能进行，需要重载为普通函数:

```cpp
Complex operator+(double r, const Complex &c){
    return Complex(c.real+r, c.imag);
}
```

我们需要把上面的函数声明称友元函数：

```cpp
class Complex{
    double real, imag;

public:
    Complex(double r, double i):real(r), imag(i){};
    Complex operator+(double r);
    friend Complex operator+(double r, const Complex &c);
}
```

## 可变长数组的实现

我们编写一个可变长整型数组，使之能如下使用：

```cpp
int main(){
    CArray a;  // 开始数组里是空的
    for(int i = 0; i < 5; i++)
        a.push_back(i);
    CArray a2, a3;
    a2 = a;
    for(int i = 0; i < a2.length(); i++)
        cout << a2[i] << " ";
    a2 = a3;
    for(int i = 0; i < a2.length(); i++)  // 这时a2.length()返回0
        cout << a2[i] << " ";
    cout << endl;

    a[3] == 100;
    CArray a4(a);
    for(int i = 0; i < a4.length(); i++)
        cout << a4[i] << " ";
    return 0;
}
```

输出：

```
0 1 2 3 4
0 1 2 100 4
```

为此我们需要做的事情：

- 用动态分配的内存来存放数组元素，需要一个指针成员变量
- 要重载 =
- 要重载 []
- 重载赋值构造函数

```cpp
class CArray{
    int size;
    int *ptr;

public:
    CArray(int s = 0);
    CArray(CArray &a);  // 复制构造函数，需要深拷贝
    ~CArray();

    void push_back(int v);
    int length(){return size;}

    CArray & operator=(const CArray &a);    // 用于数组对象间的赋值
    // [] 是双目运算符，一个操作数在[]外面，一个操作数在[]里面。
    // 返回值不能是int，如果是int 只能实现n = a[i], 而不能实现a[i] = 4
    // 非引用的函数返回值不能作为左值使用
    int &operator[](int i){
        return ptr[i];
    }
};

CArray::CArray(int s):size(s){
    if(s == 0)
        ptr = NULL;
    else
        ptr = new int[s];
}

CArray::CArray(CArray &a){
    if(!a.ptr){
        ptr = NULL;
        size = 0;
        return;
    }
    ptr = new int[a.size];
    memcpy(ptr, a.ptr, sizeof(int) * a.size);
    size = a.size;
}

CArray::~CArray(){
    if(ptr) delete [] ptr;
}

// 返回对象的引用，是为了a = b = c这样连续赋值能进行
CArray &CArray::operator=(const CArray &a){
    if(ptr == a.ptr){       // 防止a = a这样的错误
        return *this;
    }
    if(a.ptr == NULL){
        if(ptr) delete [] ptr;
        ptr = nullptr;
        size = 0;
        return *this;
    }
    // 不需要分配新的空间
    if(size < a.size){
        if(ptr) delete [] ptr;
        ptr = new int[a.size];
    }
    memcpy(ptr, a.ptr, sizeof(int) * a.size);
    size = a.size;
    return *this;
}

// 这种写法比较低效
void CArray::push_back(int v){
    if(ptr){
        int *tmp_ptr = new int[size+1];
        memcpy(tmp_ptr, ptr, sizeof(int) * size);
        delete [] ptr;
        ptr = tmp_ptr;
    }else{
        ptr = new int[1];       // 原来是空的
    }
    ptr[size++] = v;
}
```

## 流插入运算符和流提取运算符重载

cpp中`<<`和`>>`本质上就是左移和右移运算符的重载。cout是在iostream中定义的ostream类对象。

`cout << 5 << "this"`本质上的函数调用是`cout.operator<<(5).operator<<("this");`

我们想让下面的程序输出`5hello`

```cpp
class CStudent{
public:
    int n_age;
};

int main(){
    CStudent s;
    s.n_age = 5;
    cout << s << "hello";
    return 0;
}
```

otream类已经在iostream头文件中写好了，我们不可能在ostream类中再去重载，因此把重载函数写成一个全局函数。

```cpp
// 第一个参数的实参就是cout
ostream &operator<<(ostream &o, const CStudent &s){
    o << s.n_age;
    return o;
}
```

再来看一个例子，Complex是一个复数对象，我们希望执行下面的程序的得到如下的结果：

```cpp
int main(){
    Complex c;
    int n;
    cin >> c >> n;
    cout << c << ", " << n;
    return 0l
}
```

程序输入：`13.2+133i 87`，输出：`13.2+133i, 87`

```cpp
class Complex{
    double real, imag;

public:
    Complex(double r=0, double i=0):real(r), imag(i){};
    // 重载为全局函数，要访问私有成员，所以声明为友元
    friend ostream &operator<<(ostream &os, const Complex &c);
    friend istream &operator>>(istream &is, Complex &c);
};

ostream &operator<<(ostream &os, const Complex &c){
    os << c.real << "+" << c.imag << "i";
    return os;
}

istream &operator>>(istream &is, Complex &c){
    string s;
    is >> s;       // 将 a+bi 作为字符串读入
    int pos = s.find("+", 0);
    string s_tmp = s.substr(0, pos);    // 分离出代表实部的字符串
    c.real = atof(s_tmp.c_str());       // atof能将const char *指针指向的内容传唤成float
    s_tmp = s.substr(pos+1, s.length() - pos - 2);
    c.imag = atof(s_tmp.c_str());
    return is;
}
```

## 类型转换运算符重载

一个变量的名字就是类型转换运算符，如int、double等。类型转换运算符重载时不写类型，返回的类型就是那个类型本身。

```cpp
class Complex{
    double real, imag;

public:
    Complex(double r=0, double i=0):real(r), imag(i){};
    operator double () {return real;}
};

int main(){
    Complex c(1.2, 3.4);
    cout << double(c) << endl;      // 输出1.2
    double n = 2 + c;               // n = 3.2
    cout << n;
    return 0;
}
```

## 自增自减运算符的重载

前置形式的重载（重载为一元运算符重载）：

```cpp
// 重载为成员函数
T & operator++();
T & operator--();
// 重载为全局函数
T1 & operator++(T2);
T2 & operator--(T2);
```

后置形式的重载（重载为二元运算符，多写一个没用的参数）：

```cpp
// 重载为成员函数
T operator++(int);
T operator--(int);
// 重载为全局函数
T1 operator++(T2, int);
T1 opeartor--(T2, int);
```

> 在没有重载后置，只重载前置的情况下，vs中`obj++`也会调用前置，dev中`obj++`则会报错。

> 在cpp中，++a返回的是a的引用（假设a是int类型）

```cpp
#include<iostream>
using namespace std;

class CDemo{
    int n;

public:
    CDemo(int i = 0):n(i){}
    CDemo & operator++();   // 前置，cpp中前置原来就返回引用
    CDemo operator++(int);  // 后置，cpp中后置原来返回一个临时对象
    operator int() {return n;}  // 类型转换重载
    friend CDemo & operator--(CDemo &);
    friend CDemo operator--(CDemo &, int);
};

CDemo & CDemo::operator++(){
    ++n;
    return *this;
}

CDemo CDemo::operator++(int k){
    CDemo tmp(*this);   // 记录修改前的对象
    n++;
    return tmp;
}

CDemo & operator--(CDemo &d){
    d.n--;
    return d;
}

CDemo operator--(CDemo &d, int){
    CDemo tmp(d);
    d.n--;
    return tmp;
}

int main(){
    CDemo d(5);
    cout << d++ << ", ";
    cout << d << ", ";
    cout << ++d << ", ";
    cout << d;

    cout << endl;

    cout << d-- << ", ";
    cout << d << ", ";
    cout << --d << ", ";
    cout << d << endl;
    return 0;
}
```

输出结果：

```
5, 6, 7, 7
7, 6, 5, 5
```

> 由上面的例子可以看书，后置重载中会调用两次构造函数，前置的效率是高于后置的

## 运算符重载的注意事项

- c++不允许定义新的运算符
- 重载后的运算符应符合日常使用习惯
- 运算符重载不改变运算符的优先级
- 以下运算符不能被重载：`.` `.*` `::` `?:` `sizeof`
- 重载以下运算符时，必须声明为成员函数：`()` `[]` `->` `=`