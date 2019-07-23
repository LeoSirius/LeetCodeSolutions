## 思路1 利用Hash

注意这题的时间限制。如果用快排的话时间复杂度还是O(nlogn)。我们可以利用数组的下标来表示数，用数组的值来表示那个数被输入没有。利用数组随机存取的特性，我们可以在O(n)的时间复杂度内就完成计算。

这道题明确说明了输入的数各不相同。其实有相同值也可以做。用数组的值来表示下标对应的数输入了几次即可。

```cpp
#include<iostream>
using namespace std;

const int OFFSET = 500000;

int main(){
    int n, m;
    int *buf = new int[1000000]();
    while(scanf("%d%d", &n, &m) != EOF){
        for(int i = 0; i < n; ++i){
            int input;
            scanf("%d", &input);
            buf[input+OFFSET]++;
        }
        for(int i = 500000; i >= -500000; --i){
            if(buf[i+OFFSET] != 0){
                printf("%d ", i);
                m--;
            }
            if(m == 0){
                break;
            }
        }
    }
    return 0;
}
```