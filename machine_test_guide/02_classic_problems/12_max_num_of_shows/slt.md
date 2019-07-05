### 思路1 利用贪心算法的思想

选择结束时间作为贪心的对象

```cpp
#include<iostream>
#include<algorithm>
using namespace std;

struct Show{
    int s_time;
    int e_time;
    bool operator < (const Show &B) const{
        return e_time < B.e_time;
    }
};

int main(){
    int n;
    while(scanf("%d", &n) != EOF && n != 0){
        Show *shows = new Show[n];
        for(int i = 0; i < n; i++){
            scanf("%d %d", &shows[i].s_time, &shows[i].e_time);
        }
        sort(shows, shows + n);
        int total = 0;
        int current = 0;
        for(int i = 0; i < n; i++){
            if(current <= shows[i].s_time){
                total++;
                current = shows[i].e_time;
            }
        }
        printf("%d\n", total);
        delete [] shows;
    }
}
```