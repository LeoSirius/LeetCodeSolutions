### 思路1 开方后遍历

```cpp
#include<iostream>
#include<cmath>
using namespace std;

bool judge(int x){
    if(x <= 1) return false;
    int bound = (int)sqrt(x) + 1;  // sqrt比较耗时，不要放在for loop中。考虑到取整，+1多算一个
    for(int i = 2; i < bound; i++){
        if(x % i == 0) return false;
    }
    return true;
}

int main(){
    int x;
    while(scanf("%d", &x) != EOF){
        puts(judge(x) ? "yes" : "no");
    }
    return 0;
}
```