### 思路1 利用栈

用一个栈来存放所有左括号的索引。

```cpp
#include<iostream>
#include<string>
#include<stack>
using namespace std;

int main()
{
    string str;
    while (cin >> str) {
        stack<int> stk;
        string res_str = "";
        for (int i = 0; str[i]; i++) {
            if (str[i] == '(') {
                stk.push(i);
                res_str += ' ';
            } else if (str[i] == ')') {
                if (stk.empty()) {
                    res_str += '?';
                } else {
                    stk.pop();
                    res_str += ' ';
                }
            } else {
                res_str += ' ';
            }
        }
        while (!stk.empty()) {
            res_str[stk.top()] = '$';
            stk.pop();
        }
        cout << str << endl << res_str << endl;
    }
    return EXIT_SUCCESS;
}
```