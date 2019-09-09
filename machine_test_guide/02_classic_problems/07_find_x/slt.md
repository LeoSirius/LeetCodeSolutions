## 思路1 遍历查找

对于无序数组，只能遍历查找，线性时间复杂度。

```cpp
#include<iostream>
#include<vector>
using namespace std;

int
main ()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        vector<int> arr;
        for (int i = 0; i < n; i++) {
            int x; scanf("%d", &x);
            arr.push_back(x);
        }
        int target; scanf("%d", &target);
        vector<int>::const_iterator iter = arr.begin();
        for (; iter != arr.end(); iter++) {
            if (*iter == target) {
                printf("%ld\n", iter-arr.begin());
                break;
            }
        }
        if (iter == arr.end()) printf("-1\n");
    }
    return 0;
}
```