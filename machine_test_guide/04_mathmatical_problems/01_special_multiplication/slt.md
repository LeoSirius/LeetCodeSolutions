### 思路1 直接双重循环

```cpp
#include<iostream>
using namespace std;

int main(){
    char a[11], b[11];
    while(scanf("%s %s", a, b) != EOF){
        int res;
        for(int i = 0; a[i]; i++){
            for(int j = 0; b[j]; j++){
                res += (a[i] - '0') * (b[j] - '0');
            }
        }
        printf("%d\n", res);
    }
    return 0;
}
```