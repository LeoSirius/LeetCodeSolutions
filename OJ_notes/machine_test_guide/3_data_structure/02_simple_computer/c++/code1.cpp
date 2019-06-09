#include<iostream>
#include<stack>
#include<cctype>

using namespace std;

stack<char> operator_stk;
stack<double> operand_stk;

bool is_operator(char c){
    return (c == '+' || c == '-' || c == '*' || c == '/');
}

bool is_strict_lower(char a, char b){
    if(a == '+' || a == '-' && b == '*' || b == '/'){
        return true;
    }
    return false;
}

int main(){
    char input_str[201];
    while(scanf("%s", input_str) != EOF && input_str[1] != '0'){
        for(int i = 0; input_str[i]; i++){
            if(isdigit(input_str[i])){
                printf("push rand, rand = %c", input_str[i]);
                operand_stk.push(input_str[i]);
            }
        }
        for(int i = 0; input_str[i]; i++){
            if(is_operator(input_str[i])){
                if(operator_stk.empty() || is_strict_lower(input_str[i], operator_stk.top())){
                    operator_stk.push(input_str[i]);
                }else{
                    char cur_optr = operator_stk.top();
                    operator_stk.pop();

                    double a, b;
                    a = operand_stk.top();
                    operand_stk.pop();
                    b = operand_stk.top();
                    operand_stk.pop();

                    switch (cur_optr){
                    case '+':
                        operand_stk.push(a + b);
                        break;
                    case '-':
                        operand_stk.push(a - b);
                        break;
                    case '*':
                        operand_stk.push(a * b);
                        break;
                    case '/':
                        operand_stk.push(a / b);
                        break;
                    default:
                        break;
                    }
                }
            }
        }
        printf("operator_stk.empty() = %d", operator_stk.empty());
        double res = operand_stk.top();
        operand_stk.pop();
        printf("%.2lf\n", res);
    }
}