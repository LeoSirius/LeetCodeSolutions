### 思路1 利用栈

用一个栈来存放所有左括号的索引。

```cpp
#include<iostream>
#include<stack>
using namespace std;

char str[101];
char ans[101];
stack<int> stk;     // 这个stack只保存左括号的索引

int main(){
    while(scanf("%s", str) != EOF){
        for(int i = 0; str[i] != 0; ++i){
            if(str[i] == '('){
                stk.push(i);
                ans[i] = ' ';      // 暂时把左括号写成' '，后面还会检查
            }else if(str[i] == ')'){
                if(stk.empty()){
                    ans[i] = '?';  // 没有匹配成功
                }else{
                    stk.pop();
                    ans[i] = ' ';
                }
            }else{
                ans[i] = ' ';
            }
        }
        // 还有没匹配成功的左括号
        while(stk.empty() == false){
            ans[stk.top()] = '$';
            stk.pop();
        }
        printf("%s\n%s\n", str, ans);
    }
    return 0;
}
```