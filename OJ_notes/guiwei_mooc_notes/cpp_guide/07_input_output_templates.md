# 输入输出和模板

## 输入和输出

输入流对象：

- cin：与标准输入设备相连

输出流对象：

- cout：与标准输出设备相连
- cerr：与标准错误输出设备相连
- clog：与标准错误输出设备相连

在缺省情况下：cout、cerr、clog都会被打在屏幕上

```cpp
#include<iostream>
using namespace std;

int main(){
    int x, y;
    cin >> x >> y;
    freopen("test.txt", "w", stdout);    // 将标准输出重定向到test.txt文件
    if(y == 0){
        cerr << "error" << endl;    // 标准错误输出，继续输出到屏幕
    }else{
        cout << x / y;
    }
    return 0;
}
```

文件t.txt：
```
3.14 123
```

```cpp
#include<iostream>
using namespace std;

int main(){
    double f;
    int n;
    freopen("t.txt", "r", stdin);   // cin改为从t.txt中读取数据
    cin >> f >> n;
    cout << f << ", " << n << endl; // 输出 3.14 123
    return 0;
}
```