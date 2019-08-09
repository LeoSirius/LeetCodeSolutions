### 思路1 利用deque分别计算每一位

1000位的数，我们显然不能容语言内置的类型来存储。这里我们用deque来存放一个数，这样可以方便的操作最低位和最高位。

```cpp
#include<iostream>
#include<deque>
#include<string>
using namespace std;

int main(){
    string s1, s2;
    while(cin >> s1 >> s2){
        deque<int> a, b, sum;
        for(int i = 0; s1[i]; i++) a.push_back(s1[i] - '0');
        for(int i = 0; s2[i]; i++) b.push_back(s2[i] - '0');
        int carry = 0;
        while(a.size() && b.size()){
            int s = carry + a.back() + b.back();
            a.pop_back(), b.pop_back();
            sum.push_front(s % 10);
            carry = s / 10;
        }
        while(a.size()){
            int s = carry + a.back();
            a.pop_back();
            sum.push_front(s % 10);
            carry = s / 10;
        }
        while(b.size()){
            int s = carry + b.back();
            b.pop_back();
            sum.push_front(s % 10);
            carry = s / 10;
        }
        int size = sum.size();
        for(int i = 0; i < size; i++){
            cout << sum[i];
        }
        cout << endl;
    }
    return 0;
}
```