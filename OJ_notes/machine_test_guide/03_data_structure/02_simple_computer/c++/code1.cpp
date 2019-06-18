#include<iostream>
#include<stack>
#include<string>
using namespace std;

stack<char> optr_stk;
stack<double> num_stk;

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
        if(str[i] == ' ')       //  if ' ' follows a number, skip the ' '
            i++;
        return;
    }else{
        is_optr = true;
        optr = str[i];
        i += 2;             // skip current operator and the ' ' after it
        return;
    }
}

bool is_higher(char a, char b){
    if((b == '+' || b == '-') && (a == '*' || a == '/'))
        return true;
    return false;
}

double compute(double a, double b, char optr){
    if(optr == '+')
        return a + b;
    else if(optr == '-')
        return a - b;
    else if(optr == '*')
        return a * b;
    else
        return a / b;
}

int main(){
    char * str;                         // use char * to use cin.getline to get a line of string which include ' '
    while(cin.getline(str, 201)){
        string input_str(str);          // conver char * string to class string
        if(input_str.length() && input_str[0] == 0)
            break;

        while(!optr_stk.empty()) optr_stk.pop();
        while(!num_stk.empty()) num_stk.pop();

        int cur_num;
        int idx = 0;
        bool is_optr;
        char optr;
        while(true){
            if(idx >= input_str.length()){
                break;
            }
            get_next(input_str, is_optr, cur_num, optr, idx);
            if(is_optr){
                if(optr_stk.empty()){
                    optr_stk.push(optr);
                }else{
                    while(is_higher(optr_stk.top(), optr)){
                        double a = num_stk.top();
                        num_stk.pop();
                        double b = num_stk.top();
                        num_stk.pop();
                        char top_optr = optr_stk.top();
                        optr_stk.pop();
                        num_stk.push(compute(b, a, top_optr));   // notice that the sequence is reverse to input sequence
                    }
                    optr_stk.push(optr);
                }
            }else{
                num_stk.push(cur_num);
            }
        }
        //  after reading the string, compute rest operators and operands in stacks
        while(!optr_stk.empty()){
            char optr = optr_stk.top();
            optr_stk.pop();
            double a = num_stk.top();
            num_stk.pop();
            double b = num_stk.top();
            num_stk.pop();
            num_stk.push(compute(b, a, optr));
        }
        printf("%.2f\n", num_stk.top());
    }
    return 0;
}