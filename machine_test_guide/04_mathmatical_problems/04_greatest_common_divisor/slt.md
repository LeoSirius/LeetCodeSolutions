### 思路1 欧几里得算法

有递归和迭代两种写法

```cpp
#include<iostream>
using namespace std;

int gcd(int a, int b){
    return b == 0 ? a : gcd(b, a % b);
}

int main(){
    int a, b;
    while(scanf("%d %d", &a, &b) != EOF){
        printf("%d\n", gcd(a, b));
    }
    return 0;
}
```

```cpp
#include<iostream>
using namespace std;

int gcd(int a, int b){
    while(b){
        int tmp = a % b;
        a = b;
        b = tmp;
    }
    return a;
}

int main(){
    int a, b;
    while(scanf("%d %d", &a, &b) != EOF){
        printf("%d\n", gcd(a, b));
    }
    return 0;
}
```