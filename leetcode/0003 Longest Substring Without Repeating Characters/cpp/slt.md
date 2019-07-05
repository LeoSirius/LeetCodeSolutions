## 思路1 HashMap存放字符到索引的映射

start标记最近一个没有重复的字符的索引。如果当前字符已经在map中，则和start进行比较，start取最靠后的，这样保持start记录的是最近一个没有重复字符的开始索引。
另外，map和set两种容器的底层结构都是红黑树，所以容器中不会出现相同的元素，因此count()的结果只能为0和1。

```cpp
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
```