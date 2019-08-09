class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_len = 0, start = 0;
        map<char, int> char_map;

        for(int i = 0; s[i]; i++){
            if(char_map.count(s[i])){
                start = max(start, char_map[s[i]] + 1);
            }
            char_map[s[i]] = i;
            max_len = max(max_len, i - start + 1);
        }
        return max_len;
    }
};