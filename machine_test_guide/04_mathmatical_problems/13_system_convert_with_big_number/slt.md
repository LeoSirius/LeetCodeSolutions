### 思路1 

为了完成进制的转换，我们在前两题的基础上，还需要实现自定义bigInteger的除法和求模运算

```cpp
#include<iostream>
#include<deque>
#include<string>
using namespace std;

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

    // 我们预期的结果是按整除返回结果，所以如果除不尽最后的remainder直接丢掉就行了
    bigInteger operator / (int x) const{
        int remainder = 0;
        bigInteger res;
        deque<int>::const_iterator iter = value.begin();
        for(; iter != value.end(); iter++){
            int cur_dividend = remainder * 10 + *iter;
            int cur_res = cur_dividend / x;
            remainder = cur_dividend % x;
            res.value.push_back(cur_res);
        }
        while(res.value.size() && res.value[0] == 0) res.value.pop_front();
        return res;
    }

    // 求模的过程类似除法，只是随后把remainder返回，而不是丢掉。
    int operator % (int x) const{
        int remainder = 0;
        deque<int>::const_iterator iter = value.begin();
        for(; iter != value.end(); iter++){
            int cur_dividend = remainder * 10 + *iter;
            remainder = cur_dividend % x;
        }
        return remainder;
    }

    bool is_zero(){
        return (value.size() == 1 && value[0] == 0) || !value.size();
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
    int m, n;
    while(scanf("%d %d", &m, &n) != EOF){
        string x_str;
        cin >> x_str;
         // x_decimal用来保存转换成十进制的x
         // base从0次方开始，所以初始化为1
        bigInteger x_decimal, base(1);
        

        // 先转换为十进制
        int len = x_str.size();
        for(int i = len - 1; i >= 0; i--){
            int cur;
            if(x_str[i] >= '0' && x_str[i] <= '9'){
                cur = x_str[i] - '0';
            }else{
                cur = x_str[i] - 'A' + 10;
            }
            x_decimal = x_decimal + base * cur;
            base = base * m;
        }

        // 再转换为n进制，这里直接使用字符数组来存放结果
        int size = 0;
        char res[100000];
        do{
            int mod = x_decimal % n;
            if(mod >= 10) res[size++] = mod - 10 + 'a';
            else res[size++] = mod + '0';
            x_decimal = x_decimal / n;
        }while(!x_decimal.is_zero());

        for(int i = size - 1; i >= 0; i--) printf("%c", res[i]);
        printf("\n");
    }
    return 0;
}
```