### 思路1 利用栈进行计算

有两个关键点。一是处理运算符和数字的输入。二是运算符什么时候弹出计算。这里我们的标准是运算符栈里有元素，且这个元素的优先级严格大于等于当前扫描到的栈外运算符。

```cpp
#include<iostream>
#include<stack>
#include<string>
using namespace std;

stack<double> num_stk;
stack<char> optr_stk;

void get_next(string str, bool &is_optr, int &num, char &optr, int &i){
    if(i >= str.length()){
        return;
    }
    if(isdigit(str[i])){
        is_optr = false;
        num = 0;
        for(; str[i] != ' ' && str[i] != 0; i++){
            num *= 10;
            num += str[i] - '0';
        }
        if(str[i] == ' ') i++;    // 跳过数字后面的那个空格
    }else{
        is_optr = true;
        optr = str[i];
        i += 2;  // 跳过运算符后面的那个空格
    }
}

// a的优先级是否严格大于b
bool is_higher(char a, char b){
    if((b == '+' || b == '-') && (a == '*' || a == '/'))
        return true;
    return false;
}

void compute(){
    double a, b, res;
    char optr;
    // 注意数字栈的顺序和入栈是反的
    b = num_stk.top(); num_stk.pop();
    a = num_stk.top(); num_stk.pop();
    optr = optr_stk.top(); optr_stk.pop();
    switch (optr){
        case '+': res = a + b; break;
        case '-': res = a - b; break;
        case '*': res = a * b; break;
        case '/': res = a / b; break;
    }
    num_stk.push(res);
}

int main(){
    // 我们的输入包含字符，所以用cin.getline() 接受一行输入，遇到换行停止
    char * str;
    while(cin.getline(str, 201)){
        string input_str(str);   // 用char * 的str初始化一个string类的对象
        if(input_str.size() && input_str[0] == '0')
            break;
        
        while(!num_stk.empty()) num_stk.pop();
        while(!optr_stk.empty()) optr_stk.pop();

        int idx = 0;
        int cur_num;
        bool is_optr;
        char optr;
        while(true){
            if(idx >= input_str.length())
                break;
            get_next(input_str, is_optr, cur_num, optr, idx);
            if(is_optr){
                if(!optr_stk.empty()){
                    while(is_higher(optr_stk.top(), optr)){
                        compute();   // 栈中有运算符，且优先级比当前外面的高，则弹出来计算
                    }
                }
                optr_stk.push(optr); // 无论有没有弹出计算，外面的那个运算符都需要入栈
            }else{
                num_stk.push(cur_num);
            }
        }
        // 字符串读完了，但是还有运算符和数字在栈中
        while(!optr_stk.empty()){
            compute();
        }
        printf("%.2f\n", num_stk.top());
    }
    return 0;
}
```