### 思路1 素数筛法

先把10000内那些是素数，那些不是标注一下。把素数先存到一个vector中。

```cpp
#include<iostream>
#include<vector>
using namespace std;

vector<int> prime_num;
bool not_prime[10001] = {false};   // 标记是否是非素数

void init(){
    for(int i = 2; i <= 10000; i++){
        if(not_prime[i] == true) continue;   // 已经不是素数
        prime_num.push_back(i);
        // 我们从i * i开始标，因为若i * k(k < i)，则这个数必然在k时已经被标过了
        for(int j = i * i; j <= 10000; j += i){
            not_prime[j] = true;
        }
    }
}

int main(){
    init();
    int n;
    while(scanf("%d", &n) != EOF){
        int prime_size = prime_num.size();
        bool has_qualified_prime = false;
        for(int i = 0; i < prime_size; i++){
            if(prime_num[i] > n) break;
            if(prime_num[i] % 10 == 1){
                has_qualified_prime = true;
                printf("%d ", prime_num[i]);
            }
        }
        if(!has_qualified_prime) printf("-1\n");
        else printf("\n");
    }
    return 0;
}
```