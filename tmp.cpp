class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (int i = 0; s[i]; i++) {
            switch(s[i]) {
                case '(': stk.push(')'); break;
                case '[': stk.push(']'); break;
                case '{': stk.push('}'); break;
                default:
                    if (!stk.empty() && s[i] == stk.top()) stk.pop();
                    else return false;
            }
        }
        return stk.empty();
    }
};