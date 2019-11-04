#include<iostream>
#include<stack>
using  namespace std;

int main()
{
    string str;
    while (cin >> str) {
        stack<int> left_idx_stk;
        string res_str = "";
        for (int i = 0; str[i]; i++) {
            if (str[i] == '(') {
                left_idx_stk.push(i);
                res_str += ' ';
            } else if (str[i] == ')') {
                if (!left_idx_stk.empty()) {
                    left_idx_stk.pop();
                    res_str += ' ';
                } else {
                    res_str += '?';
                }
            } else {
                res_str += ' ';
            }
        }
        while (!left_idx_stk.empty()) {
            res_str[left_idx_stk.top()] = '$';
            left_idx_stk.pop();
        }
        cout << str << endl << res_str << endl;
    }
    return 0;
}