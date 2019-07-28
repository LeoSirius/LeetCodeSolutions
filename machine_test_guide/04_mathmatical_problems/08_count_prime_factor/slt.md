### 思路1 求个质因数的幂次和

以120为例，可以分解为2 * 2 * 2 * 3 * 5

```cpp
#include<iostream>
#include<vector>
#include<map>
using namespace std;

vector<int> prime_num;
bool is_non_prime[100001] = {false};   // 标记是否是非素数

void init(){
    // 输入的n最大可能有10位，我们找出它开方范围内的所有素数
    for(int i = 2; i <= 100000; i++){
        if(is_non_prime[i] == true) continue;   // 已经不是素数
        prime_num.push_back(i);
        // 这里不再从i * i开始，防止越界
        for(int j = i + i; j <= 100000; j += i){
            is_non_prime[j] = true;
        }
    }
}

int main(){
    init();
    int n;
    while(scanf("%d", &n) != EOF){
        map<int, int> mapping;  // 键是质因数，值是其对应的幂次
        int prime_size = prime_num.size();
        for(int i = 0; i < prime_size; i++){
            if(n % prime_num[i] == 0){
                mapping[prime_num[i]] = 0;
                while(n % prime_num[i] == 0){
                    mapping[prime_num[i]]++;   // 幂次初始为0，除1次加1
                    n /= prime_num[i];
                }
                if(n == 1) break;  // 已经被分解成1
            }
        }
        // 我们只测了2到100000以内的素因数。还没分解完，剩余的因数一定是一个大于100000的素因数
        if(n != 1){
            mapping[n] = 1;
        }
        int count = 0;
        map<int, int>::iterator iter = mapping.begin();
        for(; iter != mapping.end(); iter++){
            count += iter->second;
        }
        printf("%d\n", count);
    }
    return 0;
}
```