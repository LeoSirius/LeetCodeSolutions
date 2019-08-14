### 思路1 素数筛法

先把10000内那些是素数，那些不是标注一下。把素数先存到一个vector中。

```cpp
#include<iostream>
#include<vector>
using namespace std;

vector<int> prime_nums_with_right_one;      // 我们只保存个位是1的素数
bool not_prime[10001] = {false};

void init(){
    for(int i = 2; i <= 10000; i++){
        if(not_prime[i]) continue;
        if(i % 10 == 1){
            prime_nums_with_right_one.push_back(i);
        }
        for(int j = i * i; j <= 10000; j += i){
            not_prime[j] = true;
        }
    }
}

int main(){
    init();
    int n;
    while(scanf("%d", &n) != EOF){
        int size = prime_nums_with_right_one.size();
        for(int i = 0; i < size && prime_nums_with_right_one[i] < n; i++){
            printf("%d ", prime_nums_with_right_one[i]);
        }
        if(!size) printf("-1\n");
        else printf("\n");
    }
    return 0;
}
```