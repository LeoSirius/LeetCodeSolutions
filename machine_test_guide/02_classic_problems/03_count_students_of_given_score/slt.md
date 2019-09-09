## 思路1 利用hash的思路

成绩分数给定在0到100之间。我们利用一个数组，索引表示成绩，对应的值表示那个成绩的学生的个数。

```cpp
#include<iostream>
using namespace std;

int
main ()
{
    int n;
    while (scanf("%d", &n) != EOF && n != 0) {
        int scores[101] = {0};
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            scores[x]++;
        }
        int target;
        scanf("%d", &target);
        printf("%d\n", scores[target]);
    }
    return 0;
}
```