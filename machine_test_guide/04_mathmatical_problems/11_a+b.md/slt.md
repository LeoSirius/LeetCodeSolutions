### 思路1 利用deque分别计算每一位

1000位的数，我们显然不能容语言内置的类型来存储。这里我们用deque来存放一个数，这样可以方便的操作最低位和最高位。

```cpp
#include<iostream>
#include<deque>
using namespace std;

// 重载 + 运算符，支持对int类型的加法。重载输出<<
// 自定义的对象默认可以进行赋值，所以不用重载=
class bigInteger{
private:
    deque<int> value;
public:
    // 两个构造函数，一个给初始值，另一个没有
    bigInteger(){};
    bigInteger(int x){
        while(x){
            value.push_front(x % 10);
            x /= 10;
        }
    }

    void print_self(){
        deque<int>::const_iterator iter = value.begin();
        for(; iter != value.end(); iter++){
            printf("%d", *iter);
        }
        printf("\n");
    }

    bigInteger operator + (const bigInteger& B) const {
        int carry = 0;
        bigInteger res;
        deque<int>::const_reverse_iterator iter = value.rbegin(), iter_B = B.value.rbegin();
        while(iter != value.rend() || iter_B != B.value.rend() || carry){
            int v1, v2; v1 = 0, v2 = 0;
            if(iter != value.rend()){
                v1 = *iter;
                iter++;
            }
            if(iter_B != B.value.rend()){
                v2 = *iter_B;
                iter_B++;
            }
            int sum = v1 + v2 + carry;
            res.value.push_front(sum % 10);
            carry = sum / 10;
        }
        return res;
    }

    friend istream& operator >> (istream& is, bigInteger& bigInt);
};

istream& operator >> (istream& is, bigInteger& bigInt){
    string s;
    is >> s;
    bigInt.value.clear();
    for(int i = 0; s[i]; i++){
        bigInt.value.push_back(s[i] - '0');
    }
    return is;
}

int main(){
    bigInteger a, b;
    while(cin >> a >> b){
        bigInteger res = a + b;
        res.print_self();
    }
    return 0;
}
```