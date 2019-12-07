## 思路1 枚举

时间复杂度O(n^2)。下面的python实现的方法如果改成c++的话，会比cpp现在用的方法慢。因为spread_out被调用了两次。

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() <= 1) return s;
        int max_len = 1;
        int start = 0;  // we already skiped the empty case

        for (int i = 0; i < s.size();) {
            // 因为我们是从左右同时expand，如果能expand的最大长度都小于max_len，
            // 说明max_len已经是最大的了，后面的情况都不用再考虑了。
            if (max_len / 2 >= s.size() - i) break;

            int left = i, right = i;

            // 跳过重复的，下次i直接从这些重复的后面开始
            while (right < s.size() - 1 && s[right] == s[right+1]) right++;
            i = right + 1;  
            while (left >= 0 && right < s.size() && s[left] == s[right]) {
                left--;
                right++;
            }
            int new_len = right - left - 1;
            if (new_len > max_len) {
                max_len = new_len;
                start = left + 1;
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