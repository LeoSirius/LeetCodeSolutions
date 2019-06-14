#include<iostream>
#include<stack>
using namespace std;

char str[201];
stack<int> optr_stack;
stack<double> oprd_stack;

void get_next(bool & is_optr, char & ret_optr, int & ret_oprd, int & i){
    if(str[i] == 0)
        return;
    if(str[i] >= '0' && str[i] <= '9'){
        is_optr = false;
    }else{
        is_optr = true;
        ret_optr = str[i];
        i += 2;
        return;
    }
    ret_oprd = 0;
    for(; str[i] != ' ' && str[i] != 0; i++){
        ret_oprd *= 10;
        ret_oprd += str[i] - '0';
    }
    if(str[i] == ' ')
        i++;
    return;
}

bool is_lower(char a, char b){
    if((a == '+' || a == '-') && (b == '*' || b == '/'))
        return true;
    return false;
}

double compute(){

    double a, b;
    a = oprd_stack.top();
    oprd_stack.pop();
    b = oprd_stack.top();
    oprd_stack.pop();
    char optr = optr_stack.top();
    optr_stack.pop();
    double res;

    printf("in compute %f %c %f\n", a, optr, b);
    if(optr == '+')
        res = a + b;
    else if(res == '-')
        res = a - b;
    else if(res == '*')
        res = a * b;
    else if(res == '/')
        res = a / b;
    printf("push res = %f\n", res);
    oprd_stack.push(res);
    return 0;
}

int main(){
    while(gets(str)){
        if(str[0] == '0' && str[1] == 0)
            break;
        int idx = 0;
        bool is_optr;
        char ret_optr;
        int ret_oprd;
        while(!optr_stack.empty()) optr_stack.pop();
        while(!oprd_stack.empty()) oprd_stack.pop();
        while(str[idx]){
            get_next(is_optr, ret_optr, ret_oprd, idx);
            if(is_optr){
                if(optr_stack.empty() || is_lower(ret_optr, optr_stack.top())){
                    optr_stack.push(ret_optr);
                }else{
                    compute();
                }
            }else{
                oprd_stack.push(ret_oprd);
            }
        }
        compute();
        printf("oprd_stack.size() = %lu\n", oprd_stack.size());
        printf("%.2f\n", oprd_stack.top());
    }
    return -1;
}