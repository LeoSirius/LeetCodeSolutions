class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> my_map = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
        }
        int res = 0;
        for (int i = 0; i < s.size() - 1; i++) {
            if (my_map[s[i]] < my_map[s[i+1]]) res -= my_map[s[i]];
            else res += my_map[s[i]];
        }
        res += my_map[s[s.size()-1]];
        return res;
    }
};