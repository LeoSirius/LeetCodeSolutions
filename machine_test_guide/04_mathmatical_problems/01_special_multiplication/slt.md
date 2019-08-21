### 思路1 直接双重循环

结果可能会很大，我们用一个自定义的bigInt来存放。

```cpp
#include<iostream>
#include<string>
#include<deque>
using namespace std;

class bigInteger
{
private:
    deque<int> value;
public:
    bigInteger () {};
    bigInteger (int x) 
    {
        while (x) {
            value.push_front(x % 10);
            x /= 10;
        }
    }

    void print () 
    {
        deque<int>::const_iterator iter;
        for (iter = value.begin(); iter != value.end(); iter++) {
            printf("%d", *iter);
        }
        printf("\n");
    }

    bigInteger operator + (bigInteger const &B) const
    {
        int carry = 0;
        bigInteger res;
        deque<int>::const_reverse_iterator iter, iter_B;
        iter = value.rbegin();
        iter_B = B.value.rbegin();

        while (iter != value.rend() || iter_B != B.value.rend() || carry) {
            int v1, v2;
            v1 = v2 = 0;
            if (iter != value.rend()) {
                v1 = *iter;
                iter++;
            }
            if (iter_B != B.value.rend()) {
                v2 = *iter_B;
                iter_B++;
            }
            int sum = v1 + v2 + carry;
            res.value.push_front(sum % 10);
            carry = sum / 10;
        }
        return res;
    }
};

int main()
{
    string a, b;
    while (cin >> a >> b) {
        bigInteger res;
        for (int i = 0; i < a.size(); i++) {
            for (int j = 0; j < b.size(); j++) {
                int cur_mutiple = (a[i] - '0') * (b[j] - '0');
                res = res + cur_mutiple;
            }
        }
        res.print();
    }
    return 0;
}
```