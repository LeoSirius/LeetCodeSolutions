### 思路1 自己实现一个支持乘法的类型

由于阶乘可能涉及很大的数，内建类型肯定是不够用的，自己实现一个支持乘法的类型。

```cpp
#include<iostream>
#include<deque>
using namespace std;

// 重载 * 运算符，支持对int类型的乘法
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

    bigInteger operator * (int x) const {
        int carry = 0;
        bigInteger res;
        deque<int>::const_reverse_iterator iter = value.rbegin();
        for(; iter != value.rend(); iter++){
            int multiple = *iter * x + carry;
            //cout << "multiple = " << multiple << endl;
            res.value.push_front(multiple % 10);
            carry = multiple / 10;
        }
        if(carry) res.value.push_front(carry);
        return res;
    }
};

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        bigInteger res(1);
        for(int i = 1; i <= n; i++){
            res = res * i;
        }
        res.print_self();
    }
    return 0;
}
```
