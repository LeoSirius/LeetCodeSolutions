class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        unordere_dmap<char, char> my_map = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'},
        }
        for (int i = 0; s[i]; i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                stk.push(s[i]);
            } else {
                if (stk.empty()) return false;
                char top = stk.top(); stk.pop();
                if (my_map[top] != s[i]) return false;
            }
        }
        return stk.empty();
    }
};