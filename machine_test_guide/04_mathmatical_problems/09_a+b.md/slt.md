### 思路1 自己实现一个bitInt类型，支持加法运算

1000位的数，我们显然不能容语言内置的类型来存储。这里我们用deque来存放一个数，这样可以方便的操作最低位和最高位。

重载 + 运算符。重载输入>>。自定义的对象默认可以进行赋值，所以不用重载

```cpp
#include<iostream>
#include<deque>
using namespace std;

class BigInteger
{
private:
    deque<int> value;

public:
    void print()
    {
        deque<int>::const_iterator iter;
        for (iter = value.begin(); iter != value.end(); iter++) {
            printf("%d", *iter);
        }
    }

    friend istream &operator >> (istream &is, BigInteger &bigInt);

    BigInteger operator + (BigInteger &other) const
    {
        int carry = 0;
        deque<int>::const_reverse_iterator iter, o_iter;
        iter = value.rbegin();
        o_iter = other.value.rbegin();
        BigInteger res;
        while (iter != value.rend() || o_iter != other.value.rend() || carry) {
            int v1 = iter != value.rend() ? *iter++ : 0;
            int v2 = o_iter != other.value.rend() ? *o_iter++ : 0;
            int sum = v1 + v2 + carry;
            res.value.push_front(sum%10);
            carry = sum / 10;
        }
        return res;
    }
};

istream &operator >> (istream &is, BigInteger &bigInt)
{
    string s;
    cin >> s;
    bigInt.value.clear();
    for (int i = 0; s[i]; i++) {
        bigInt.value.push_back(s[i] - '0');
    }
    return is;
}

int main()
{
    BigInteger a, b;
    while (cin >> a >> b) {
        a = a + b;
        a.print();
        cout << endl;
    }
    return 0;
}
```