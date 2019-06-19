class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> char_map;
        int start = 0;
        int max_len = 0;
        for(int i = 0; i < s.size(); i++){
            if(char_map.count(s[i])){
                start = max(start, char_map[s[i]] + 1);
            }
            char_map[s[i]] = i;
            max_len = max(max_len, i - start + 1);
        }
        return max_len;
    }
};