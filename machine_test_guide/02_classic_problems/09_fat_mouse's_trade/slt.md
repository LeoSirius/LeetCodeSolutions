### 思路1 使用贪心算法

一个房间java bean不用一次全部买完，所以用贪心算法可以得到最优解。

```cpp
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

struct Room
{
    double javabean;
    double catFood;
    double java_per_food;

    bool
    operator < (Room const &other) const
    {
        return java_per_food > other.java_per_food;
    }
};

int
main ()
{
    int m, n;
    while (scanf("%d %d", &m, &n) != EOF && !(m == -1 && n == -1)) {
        vector<Room> rooms;
        for (int i = 0; i < n; i++) {
            Room room;
            scanf("%lf %lf", &room.javabean, &room.catFood);
            room.java_per_food = room.javabean / room.catFood;
            rooms.push_back(room);
        }
        sort(rooms.begin(), rooms.end());
        double total_bean = 0;
        for (int i = 0; i < rooms.size() && m > 0; i++) {
            if (m > rooms[i].catFood) {
                total_bean += rooms[i].javabean;
                m -= rooms[i].catFood;
            } else {
                total_bean += m * rooms[i].java_per_food;
                m = 0;
            }
        }
        printf("%.3f\n", total_bean);
    }
    return EXIT_SUCCESS;
}
```