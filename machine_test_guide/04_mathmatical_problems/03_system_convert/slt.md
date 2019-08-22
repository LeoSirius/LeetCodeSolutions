### 思路1 先转化为十进制，再转化为对应进制

对于要在头部插入和删除的，还是用deque比较方便。

```cpp
#include<iostream>
#include<string>
#include<deque>
using namespace std;

int main()
{
    int a, b;
    string n;
    while (cin >> a >> n >> b) {
        long long decimal = 0, base = 1;
        for (int i = n.size() - 1; i >= 0; i--) {
            int cur_num = 0;
            if (n[i] >= '0' && n[i] <= '9') cur_num = n[i] - '0';
            else if (n[i] >= 'A' && n[i] <= 'Z') cur_num = n[i] - 'A' + 10;
            decimal += cur_num * base;
            base *= a;
        }

        deque<char> res;
        while (decimal) {
            int mod = decimal % b;
            decimal /= b;
            if (mod < 10) res.push_front(mod + '0');
            else res.push_front(mod - 10 + 'A');
        }
        deque<char>::const_iterator iter;
        for (iter = res.begin(); iter != res.end(); iter++)
            printf("%c", *iter);
        printf("\n");
    }
    return 0;
}
```