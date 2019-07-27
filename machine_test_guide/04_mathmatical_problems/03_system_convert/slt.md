### 思路1 先转化为十进制，再转化为对应进制

```cpp
#include<iostream>
using namespace std;

int main(){
    int a, b;
    char str[40];
    while(scanf("%d %s %d", &a, str, &b) != EOF){
        int decimal = 0;
        int len = strlen(str);
        int base = 1;       // 权重，从0次方开始
        for(int i = len - 1; i >= 0; i--){
            int x;
            if(str[i] >= '0' && str[i] <= '9'){
                x = str[i] - '0';
            }else if(str[i] >= 'a' && str[i] <= 'z'){
                x = str[i] - 'a' + 10;
            }else{
                x = str[i] - 'A' + 10;
            }
            decimal += x * base;
            base *= a;
        }
        char ans[40];
        int size = 0;
        do{
            int x = decimal % b;
            ans[size++] = (x < 10) ? x + '0' : x - 10 + 'A';
            decimal /= b;
        }while(decimal);
        for(int i = size-1; i >= 0; i--){
            printf("%c", ans[i]);
        }
        printf("\n");
    }
    return 0;
}
```