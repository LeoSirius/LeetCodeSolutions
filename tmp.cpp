#include<iostream>
#include<string>
#include<stack>
using namespace std;

stack<char> optr_stk;
stack<float> num_stk;

void compute()
{
    if (num_stk.empty() || optr_stk.empty()) return;
    double b = num_stk.top(); num_stk.pop();
    double a = num_stk.top(); num_stk.pop();
    char optr = optr_stk.top(); optr_stk.pop();

    cout << a << " " << optr << " " << b << " = " << endl;

    switch (optr) {
        case '+' : num_stk.push(a + b); break;
        case '-' : num_stk.push(a - b); break;
        case '*' : num_stk.push(a * b); break;
        case '/' : num_stk.push(a / b); break;
    }
}

bool is_higher(char a, char b)
{
    if ((a == '*' || a == '/') && (b == '+' || b == '-')) return true;
    else return false;
}

int main()
{
    string str;
    char in_str[201];
    while (cin.getline(in_str, 200)) {
        str = in_str;
        char ch;
        for (int i = 0; (ch = str[i]); i++) {
            if (ch == ' ') continue;
            if (ch >= '0' && ch <= '9') {
                num_stk.push(ch - '0');
            } else {
                while (!optr_stk.empty() && is_higher(optr_stk.top(), ch)) {
                    compute();
                }
                optr_stk.push(ch);
            }
        }
        while (!optr_stk.empty()) compute();
        printf("%.2f\n", num_stk.top());
    }
    return 0;
}