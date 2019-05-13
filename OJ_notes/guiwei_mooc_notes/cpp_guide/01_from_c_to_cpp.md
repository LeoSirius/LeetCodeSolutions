# from c to cpp

## 引用

### 注意三点

- 定义引用时一定要将其初始化成引用某个变量
- 初始化后，它就一直引用该变量，不会再引用别的变量（引用从一而终）
- 引用只能引用变量，不能引用常量和表达式

例子：用引用交换两个变量的值

```cpp
void swap(int & a, int & b){
    int tmp;
    tmp = a; a = b; b = tmp;
}
int n1, n2;
swap(n1, n2); // 交换n1和n2的值
```

引用作为函数的返回值

```cpp
int n = 4;
int & SetValue() {return n;}
int main(){
    SetValue() = 40;  // 等价于把40赋值给全局变量n
    cout << n;        // 输出40
    return 0;
}
```

### 常引用

- 不能通过常引用去修改引用的内容

```cpp
int n = 100;
const int & r = n;
r = 200; // 编译出错
n = 300; // 没问题
```

### 常引用和非常引用的转换

- const T & 和T & 是不同的类型！！！
- T &类型的引用可与用来初始化const T & 类型的引用
- const T & 类型的引用和const T 类型的变量不能用来初始化T & 类型的引用，除非进行强制类型转换。