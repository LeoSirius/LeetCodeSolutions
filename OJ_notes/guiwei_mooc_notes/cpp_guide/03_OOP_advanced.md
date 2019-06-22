# OOP Advanced

## this指针

cpp刚出来的时候没有编译器，会被翻译成c然后用c的编译器。我们来看一个cpp程序翻译的c程序

cpp程序

```cpp
class CCar{
public:
    int price;
    void SetPrice(int p);
};

void CCar::SetPrice(int p){
    price = p;
}

int main(){
    CCar car;
    car.SetPrice(200);
    return 0;
}
```

c程序，成员函数被翻译成全局函数

```c
struct CCar{
    int price;
};

void SetPrice(struct CCar *this, int p){
    this->price = p;
}

int main(){
    struct CCar car;
    SetPrice(&cat, 200);
    return 0;
}
```

可以看出，为了表明当前的对象，我们多用了一个this指针作为参数。实际上，cpp编译的机器指令中，成员函数都会多一个参数。

this指针的作用：指向成员函数所作用的对象。

再看一个例子：

cpp程序

```cpp
class A{
    int i;

public:
    void Hello(){cout << "hello" << endl;}
    // 会被翻译成：void Hello(A *this){cout << "hello" << endl;}
};

int main(){
    A *p = NULL;
    p->Hello(); // 翻译后的调用Hello(p);
}
```

这段程序能正确执行，并输出`hello`。我们可以看到函数中并没有对对象this进行使用，所以能正常运行。但如果改成下面的代码，则会出错

```cpp
class A{
    int i;

public:
    void Hello(){
        cout << i << "hello" << endl;
    }
};

int main(){
    A *p = NULL;
    p->Hello();
}
```

因为`i`翻译后是`this->i`，而`this`指针是空指针，所以出错。

>注意在静态成员函数中不能使用`this`指针！因为静态成员函数并不具体作用于某个对象。

## 静态成员

静态成员：在声明前加`static`关键字的成员。静态成员不需要通过对象就能访问。

- 普通成员变量每个对象各自有一份，而静态成员变量只有一份，为所有对象共享。
- 普通成员函数必须具体作用在某个对象上，而静态成员函数并不具体作用于某个对象。

>注意sizeof运算符不会计算静态成员变量。

访问静态成员：

1. 类名::对象名
   `Rectangle::PrintTotal()`
2. 对象名.成员名
   `Rectangle r; r.PrintTotal()`
3. 指针->成员名
   `Rectangle *p = &r; p->PrintTotal();`
4. 引用.成员名
   `Rectangle &ref = r; ref.PrintTotal();`

> 第二、三、四种方法虽然通过对象r来调用，但并不作用在r上。

- 静态成员变量实际上是全局变量，哪怕一个对象都不存在，静态成员变量也存在。
- 静态成员函数实际上是全局函数

设置静态成员机制的目的是将某些和类紧密关联的全局变量和函数写到类里面去，看上去更像一个整体，使代码更好维护。

> 注意在静态成员函数中，不能访问非静态成员变量，也不能调用非静态成员函数。

## 成员对象和封闭类

封闭类（enclosing）：有成员对象的类

封闭类构造函数和析构函数的执行顺序：

- 封闭类对象生成时，先执行所有对象成员的构造函数，然后才执行封闭类的构造函数。
- 封闭类对象消亡时，先执行封闭类的析构函数，然后才执行对象成员的析构函数。
- 对象成员的构造函数调用的顺序与对象成员在类中的说明次序一致，与它们在成员初始化列表中的次序无关。

封闭类的复制构造函数：

```cpp
class A{
public:
    A(){cout << "default" << endl;}
    A(A &a){cout << "copy" << endl;}
};

class B{
    A a;
};

int main(){
    B b1, b2(b1);
    return 0;
}
```

输出：

```
default
copy
```

`b2.a`是用`A`类的复制构造函数初始化的。而且调用复制构造函数时的实参就是`b1.a`

## 常量对象、常量成员函数和常引用

常量对象定以后后续不能再被修改。常量对象上不能执行非常量成员函数，可以执行常量成员函数。

常量成员函数：常量成员函数执行期间不应该修改其所作用的对象。因此，在常量成员函数中不能修改成员变量的值，也不能调用同类的非常量成员函数。（静态成员变量和静态成员函数除外，因为它们实际上是全局的）

> 注意一个类的两个成员函数名字和参数表都一样，一个是`const`，一个不是，这算重载。

我们来看一个例子：

```cpp
class CTest{
private:
    int n;

public:
    CTest(){n = 1;}
    int GetValue() const {return n;}
    int GetValue() {return n * 2;}
};

int main(){
    const CTest obj1;
    CTest obj2;
    cout << obj1.GetValue() << ", " << obj2.GetValue() << endl;
    return 0;
}
```

输出:

```
1, 2
```

## 友元

友元分为友元函数和友元类两种

- 友元函数：一个类的友元函数（友元函数不是这个类的成员函数）可以访问该类的私有成员。
- 友元类：如果A是B的友元类，那么A的成员函数可以访问B的私有成员。

> 友元类之间的关系不能传递，不能继承