### 思路1 求个质因数的幂次和

以120为例，可以分解为2 * 2 * 2 * 3 * 5

```cpp
#include<iostream>
#include<vector>
#include<map>
#include<cstring>
using namespace std;

vector<int> prime_nums;
bool is_prime[100001];

void init(){
    // 输入的n最大可能有10位，我们找出它开方范围内的所有素数
    memset(is_prime, true, sizeof(is_prime)); // 使用memset初始化布尔数组为true
    for(int i = 2; i <= 100000; i++){
        if(!is_prime[i]) continue;
        prime_nums.push_back(i);
        // 这里不再从i * i开始，防止越界，这里i很大
        for(int j = i + i; j <= 100000; j+=i){
            is_prime[j] = false;
        }
    }
}

int main(){
    init();
    int n;
    while(scanf("%d", &n) != EOF){
        map<int, int> prime_power_map;      // 键是质因数，值是其对应的幂次
        int prime_size = prime_nums.size();
        cout << "prime_size = " << prime_size << endl;
        for(int i = 0; i < prime_size; i++){
            if(n % prime_nums[i] == 0){
                prime_power_map[prime_nums[i]] = 0;
                while(n % prime_nums[i] == 0){
                    prime_power_map[prime_nums[i]]++;  // 幂次初始为0，除1次加1
                    n /= prime_nums[i];
                }
                if(n == 1) break;   // 已经被分解成1
            }
        }
        // 我们只测了2到100000以内的素因数。还没分解完，剩余的因数一定是一个大于100000的素因数
        if(n != 1) prime_power_map[n] = 1;
        int count = 0;
        map<int, int>::const_iterator iter = prime_power_map.begin();
        for(; iter != prime_power_map.end(); iter++){
            count += iter->second;
            cout << "iter->second = " << iter->second << endl;
        }
        printf("%d\n", count);
    }
    return 0;
}
```