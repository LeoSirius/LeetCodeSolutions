### 思路1 先转化为十进制，再转化为对应进制

对于要在头部插入和删除的，还是用deque比较方便。

```cpp
#include<iostream>
#include<deque>
using namespace std;

int main()
{
    int a, b;
    string n;
    while (cin >> a >> n >> b) {
        int base = 1;
        int dec = 0;
        for (int i = n.size() - 1; i >= 0; i--) {
            int cur;
            if (n[i] >= '0' && n[i] <= '9') cur = n[i] - '0';
            else cur = n[i] - 'A' + 10;
            dec += + cur * base;
            base *= a;
        }
        deque<char> res;
        deque<char>::const_iterator iter;
        while (dec) {
            int mod = dec % b;
            res.push_front("0123456789ABCDEF"[mod]);
            dec /= b;
        }
        for (iter = res.begin(); iter != res.end(); iter++) {
            printf("%c", *iter);
        }
        printf("\n");
    }
    return 0;
}
```