### 思路1 利用栈进行计算

有两个关键点。一是处理运算符和数字的输入。二是运算符什么时候弹出计算。这里我们的标准是运算符栈里有元素，且这个元素的优先级严格大于等于当前扫描到的栈外运算符。最后，不管有没有运算，栈外运算符都要运算符栈。

```cpp
#include<iostream>
#include<string>
#include<stack>
using namespace std;

stack<double> num_stk;
stack<char> optr_stk;

void get_next(string str, int &i, bool &is_optr, char &optr, int &num)
{
    if (i >= str.size()) return;
    if (isdigit(str[i])) {
        is_optr = false;
        num = 0;
        while (i <= str.size() && isdigit(str[i])) {
            num = num * 10 + str[i] - '0';
            i++;
        }
        if (str[i] == ' ') i++;   // 跳过空格
    } else {
        is_optr = true;
        optr = str[i];
        i += 2;         // 跳过当前的运算符和空格
    }
}

bool is_higher(char a, char b)
{
    if ((a == '*' || a == '/') && (b == '+' || b == '-')) return true;
    else return false;
}

void compute()
{
    if (num_stk.empty() || optr_stk.empty()) return;
    double b = num_stk.top(); num_stk.pop();
    double a = num_stk.top(); num_stk.pop();
    char optr = optr_stk.top(); optr_stk.pop();


    switch (optr) {
        case '+' : num_stk.push(a + b); break;
        case '-' : num_stk.push(a - b); break;
        case '*' : num_stk.push(a * b); break;
        case '/' : num_stk.push(a / b); break;
    }
}

int main()
{
    string in_str;
    char str[201];
    while (cin.getline(str, 200)) {
        in_str = str;
        if (in_str.size() == 1 && in_str[0] == '0') break;
        while (!num_stk.empty()) num_stk.pop();
        while (!optr_stk.empty()) optr_stk.pop();

        int cur_num;
        char cur_optr;
        bool is_optr;
        int index = 0;
        while (index < in_str.size()) {
            get_next(in_str, index, is_optr, cur_optr, cur_num);
            if (is_optr) {
                while (!optr_stk.empty() && is_higher(optr_stk.top(), cur_optr)) {
                    compute();
                }
                optr_stk.push(cur_optr);
            } else {
                num_stk.push(cur_num);
            }
        }
        while (!optr_stk.empty()) compute();
        printf("%.2f\n", num_stk.top());
    }
    return EXIT_SUCCESS;
}
```