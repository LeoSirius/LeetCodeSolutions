### 思路1 利用贪心算法的思想

然后对结束时间按照从小到大的顺序进行排序，如果结束的时间相同的话，就将开始的时间按照从大到小的顺序排序。

```cpp
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

struct Show
{
    int s, e;

    bool operator < (Show const &other) const {
        if (e != other.e) {
            return e < other.e;
        } else {
            return s > other.s;
        }
    }
};

int
main ()
{
    int n;
    while (scanf("%d", &n) != EOF && n != 0) {
        vector<Show> shows;
        for (int i = 0; i < n; i++) {
            Show show;
            scanf("%d %d", &show.s, &show.e);
            shows.push_back(show);
        }
        sort(shows.begin(), shows.end());
        int cur_time = 0;
        int show_cnt = 0;
        for (int i = 0; i < shows.size(); i++) {
            if (cur_time <= shows[i].s) {
                show_cnt++;
                cur_time = shows[i].e;
            }
        }
        printf("%d\n", show_cnt);
    }
    return EXIT_SUCCESS;
}
```