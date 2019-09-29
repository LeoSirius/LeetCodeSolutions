### 思路1 自己实现一个支持乘法的类型

由于阶乘可能涉及很大的数，内建类型肯定是不够用的，自己实现一个支持乘法的类型。
重载 * 运算符，支持对int类型的乘法。自定义的对象默认可以进行赋值，所以不用重载=

```cpp
#include<iostream>
#include<deque>
using namespace std;

class BigInteger
{
private:
    deque<int> value;

public:
    BigInteger() {};
    BigInteger(int x)
    {
        value.clear();
        while(x){
            value.push_front(x % 10);
            x /= 10;
        }
    }

    void print()
    {
        deque<int>::const_iterator iter;
        for (iter = value.begin(); iter != value.end(); iter++) {
            printf("%d", *iter);
        }
    }

    BigInteger operator * (int k) const
    {
        int carry = 0;
        BigInteger res;
        deque<int>::const_reverse_iterator iter;
        iter = value.rbegin();
        while (iter != value.rend() || carry) {
            int v1 = iter != value.rend() ? *iter++ : 0;
            int mul = v1 * k + carry;
            res.value.push_front(mul % 10);
            carry = mul / 10;
        }
        return res;
    }



};

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        BigInteger res(n);
        for (int i = 1; i < n; i++) {
            res = res * i;
        }
        res.print();
        printf("\n");
    }
    return 0;
}
```
