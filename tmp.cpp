class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for(char&c : s){
            switch(c){
                case '[': stk.push(']'); break;
                case '(': stk.push(')'); break;
                case '{': stk.push('}'); break;
                default:
                    if(stk.size() == 0 || c != stk.top()) return false;
                    else stk.pop();
            }
        }
        return stk.empty();
    }
};