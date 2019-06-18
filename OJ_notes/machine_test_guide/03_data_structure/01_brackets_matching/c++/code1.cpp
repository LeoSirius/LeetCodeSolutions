#include<iostream>
#include<stack>
using namespace std;

stack<int> stk;

int main(){
    char str[101];
    while(scanf("%s", str) != EOF){
        char output[101];
        for(int i = 0; str[i]; i++){
            if(str[i] == ')'){
                if(stk.empty()){
                    output[i] = '?';
                }else{
                    stk.pop();
                    output[i] = ' ';
                }
            }else if(str[i] == '('){
                stk.push(i);
                output[i] = ' ';
            }else{
                output[i] = ' ';
            }
        }
        while(!stk.empty()){
            output[stk.top()] = '$';
            stk.pop();
        }
        puts(str);
        puts(output);
    }
    return 0;
}