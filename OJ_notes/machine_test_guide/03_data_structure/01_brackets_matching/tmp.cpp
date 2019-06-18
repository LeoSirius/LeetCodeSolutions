#include<iostream>
#include<string>
#include<stack>
using namespace std;

stack<int> stk;     // this stack save the index of left brackets

int main(){
    string str;
    string ans;
    while(cin >> str){
        string ans(str.length(), ' ');   // init ans string with ' ' of str.length();
        for(int i = 0; str[i]; i++){
            if(str[i] == '('){
                stk.push(i);
            }else if(str[i] == ')'){
                if(stk.empty()){
                    ans[i] = '?';     // has right brackets, but lack left, so could not match
                }else{
                    stk.pop();
                }
            }
        }
        while(!stk.empty()){
            int idx = stk.top();
            stk.pop();
            ans[idx] = '&';
        }
        printf("%s\n", str.c_str());
        printf("%s\n", ans.c_str());
    }
    return 0;
}