## 思路1 枚举

时间复杂度O(n^2)

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        if(s.empty()) return "";
        if(s.size() == 1) return s;
        int start = 0;
        int max_len = 1;        // we already skiped the empty case

        for(int i = 0; i < s.size();){
            // 因为我们是从左右同时expand，如果能expand的最大长度都小于max_len，
            // 说明max_len已经是最大的了，后面的情况都不用再考虑了。
            if(s.size() - i <= max_len / 2) break;  // 求得的长度
            int left = i, right = i;
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
```

遍历每个字符。对每个字符从中间往两边扩散比较。找到最长的。

```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            tmp = self.spread_out(s, i, i)  # case 'aba'
            if len(tmp) > len(res):
                res = tmp
            tmp = self.spread_out(s, i, i+1) # case 'abba'
            if len(tmp) > len(res):
                res = tmp
        return res

    def spread_out(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 最后一次的left，right的索引已经不再符合条件，所以返回的时候不要包含它们
        return s[left+1:right]
```