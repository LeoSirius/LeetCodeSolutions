### 思路1 使用二分求幂

这道题有两个要点，一是使用二分求幂加快速度，二是处理的数据很大，且最后只输出三位数。所以我们在中途中也只保存三位数。

```cpp
#include<iostream>
using namespace std;

int main(){
    int a, b;
    while(scanf("%d %d", &a, &b) != EOF && (a != 0 && b != 0)){
        int res = 1;
        while(b){
            if(b % 2 == 1){
                res *= a;       // 如果是几次幂，则把当前的a^k乘到res上
                res %= 1000;
            }
            b /= 2;
            a *= a;
            a %= 1000;
        }
        printf("%d\n", res);
    }
    return 0;
}
```