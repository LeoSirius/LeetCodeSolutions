## 思路1 利用hash的思路

成绩分数给定在0到100之间。我们利用一个数组，索引表示成绩，对应的值表示那个成绩的学生的个数。

```cpp
#include<iostream>
using namespace std;

int main(){
    int n;
    while(scanf("%d", &n) != EOF && n != 0){
        int *hashing = new int[101]{0};  // 这样会初始化为0, c++11可以这样写
        for(int i = 0; i < n; i++){
            int input_score;
            scanf("%d", &input_score);
            hashing[input_score]++;
        }
        int target_score;
        scanf("%d", &target_score);
        printf("%d\n", hashing[target_score]);
        delete [] hashing;
    }
    return 0;
}
```