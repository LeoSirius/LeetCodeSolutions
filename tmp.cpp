class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() <= 1) return s;
        int max_len = 1, start = 0;
        for (int i = 0; i < s.size();)
        {
            int left, right;
            left = right = i;
            while (right < s.size() - 1 && s[right] == s[right+1]) right++;
            i = right + 1;
            while (left > 0 && right < s.size() - 1 && s[left-1] == s[right+1])
            {
                left--; right++;
            }
            int new_len = right - left + 1;
            if (new_len > max_len)
            {
                max_len = new_len;
                start = max(start, left);
            }
            while(right < s.size()-1 && s[right+1] == s[right]) right++;
            i = right + 1;    // 跳过重复的，下次i直接从这些重复的后面开始
            while(right < s.size()-1 && left > 0 && s[right+1] == s[left-1]){
                right++;
                left--;
            }
            int new_len = right - left + 1;
            if(new_len > max_len){
                start = left;
                max_len = new_len;
            }
         }
        return s.substr(start, max_len);
    }
};