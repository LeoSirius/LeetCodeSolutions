### 思路1 利用栈

用一个栈来存放所有左括号的索引。

```cpp
#include<iostream>
#include<stack>
using namespace std;

int main(){
    string input_str;
    string res_str;
    stack<int> stk;
    while(getline(cin, input_str)){
        while(!stk.empty()) stk.pop();
        for(int i = 0; i < input_str.length(); ++i){
            if(input_str[i] == '('){
                stk.push(i);
                res_str += " ";
            }else if(input_str[i] == ')'){
                if(!stk.empty()){
                    stk.pop();
                    res_str += " ";
                }else{
                    res_str += "?";
                }
            }else{
                res_str += " ";
            }
        }
        while(!stk.empty()){
            res_str[stk.top()] = '$';
            stk.pop();
        }
        cout << input_str << endl;
        cout << res_str << endl;
    }
    return 0;
}
```