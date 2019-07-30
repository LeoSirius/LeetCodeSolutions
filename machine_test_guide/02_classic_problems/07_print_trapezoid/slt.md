## 思路1 找规律直接输出

这一类输出图形的体规律性较强，找到规律直接输出即可。

```cpp
#include<iostream>
using namespace std;

int main(){
    int h;
    while(scanf("%d", &h) != EOF){
        int num_of_space = (h - 1) * 2;
        int num_of_star = h;
        for(int i = 0; i < h; i++, num_of_space -= 2, num_of_star += 2){
            for(int j = 0; j < num_of_space; j++){
                printf(" ");
            }
            for(int j = 0; j < num_of_star; j++){
                printf("*");
            }
            printf("\n");
        }
    }
}
```