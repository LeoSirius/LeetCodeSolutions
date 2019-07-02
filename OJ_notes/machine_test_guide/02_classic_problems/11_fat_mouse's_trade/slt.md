### 思路1 使用贪心算法

一个房间java bean不用一次全部买完，所以用贪心算法可以得到最优解。

```cpp
#include<iostream>
#include<algorithm>
using namespace std;

struct Room{
    double java_beans;
    double food;
    double ratio;   // java_beans per food
    bool operator < (const Room B) const{
        return ratio > B.ratio;     // 重载，使得按照ratio的降序排列
    }
};

int main(){
    int M, N;
    while(scanf("%d %d", &M, &N) != EOF && (M != -1 || N != -1)){
        Room *rooms = new Room[N];
        for(int i = 0; i < N; i++){
            scanf("%lf %lf", &rooms[i].java_beans, &rooms[i].food);
            rooms[i].ratio = rooms[i].java_beans / rooms[i].food;
        }
        sort(rooms, rooms + N);
        double total_java_beans = 0;
        for(int i = 0; i < N && M != 0; i++){
            if(M >= rooms[i].food){
                total_java_beans += rooms[i].java_beans;
                M -= rooms[i].food;
            }else{
                total_java_beans += rooms[i].ratio * M;
                M = 0;
            }
        }
        printf("%.3f\n", total_java_beans);
    }
}
```