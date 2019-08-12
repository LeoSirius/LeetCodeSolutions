#include<iostream>
#include<stack>
#include<string>
using namespace std;

stack<double> num_stk;
stack<char> optr_stk;

void get_next(string str, int& i, bool& is_optr, char &optr, int &num){
    if(i >= str.length()) return;
    if(isdigit(str[i])){
        is_optr = false;
        num = 0;
        while(i < str.length() && isdigit(str[i])){
            num = num * 10 + str[i] - '0';
            i++;
        }
        if(str[i] == ' ') i++;   // 跳过空格
    }else{
        is_optr = true;
        optr = str[i];
        i += 2;  // 跳过当前的运算符和空格
    }
}

bool is_higher(char a, char b){
    if((a == '*' || a == '/') && (b == '+' || b == '-')) return true;
    return false;
}

void compute(){
    double a, b;
    char optr;
    if(num_stk.empty() || optr_stk.empty()) return;
    b = num_stk.top(); num_stk.pop();
    a = num_stk.top(); num_stk.pop();
    optr = optr_stk.top(); optr_stk.pop();

    switch(optr){
        case '+': num_stk.push(a+b); break;
        case '-': num_stk.push(a-b); break;
        case '*': num_stk.push(a*b); break;
        case '/': num_stk.push(a/b); break;
    }
}

int main(){
    char* str;
    string input_str;
    while(cin.getline(str, 200)){
        input_str = str;
        if(!input_str.length() || (input_str.length() == 1 && input_str[0] == '0'))
            break;
        while(!num_stk.empty()) num_stk.pop();
        while(!optr_stk.empty()) optr_stk.pop();

        int idx = 0;
        int cur_num;
        char cur_optr;
        bool is_optr;
        while(idx < input_str.length()){
            get_next(input_str, idx, is_optr, cur_optr, cur_num);
            if(is_optr){
                while(!optr_stk.empty() && is_higher(optr_stk.top(), cur_optr)){
                    compute();
                }
                optr_stk.push(cur_optr);
            }else{
                num_stk.push(cur_num);
            }
        }
        while(!optr_stk.empty()){
            compute();
        }
        printf("%.2f\n", num_stk.top());
    }
    return 0;
}