### 思路1 先直接求和，在转换进制

```cpp
#include<iostream>
using namespace std;

int main(){
    long long a, b;     // a b为32位，但是加起来可能超过
    int m;
    while(scanf("%d", &m) != EOF && m){
        scanf("%lld %lld", &a, &b);
        a = a + b;
        int res[50], size = 0;
        do{
            res[size++] = a % m;
            a /= m;
        }while(a);
        for(int i = size - 1; i >= 0; i--){
            printf("%d", res[i]);
        }
        printf("\n");
    }
    return 0;
}
```