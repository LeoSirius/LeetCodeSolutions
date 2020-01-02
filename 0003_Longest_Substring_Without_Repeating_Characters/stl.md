## 思路1 HashMap存放字符到索引的映射

如果用传统的双重循环遍历每个子串的话，时间复杂度是O(n^2)。我们这里使用map的时间复杂度只有O(n^logn)。（假定map search的时间复杂度为O(n^logn)，比如c++中）

map的key为s中的字符，value为字符的索引

start标记最近一个没有重复的字符的索引。如果当前字符已经在map中，则和start进行比较，start取最靠后的，这样保持start记录的是最近一个没有重复字符的开始索引。
另外，map和set两种容器的底层结构都是红黑树，所以容器中不会出现相同的元素，因此count()的结果只能为0和1。

注意start只能向前移动`start = max(start, char_map[s[i]] + 1);`。列入`abba`，当i扫描到最后一个a时，第一个a在map中，如果不加max，则start会往后回去。

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> char_map;
        int start = 0, max_len = 0;
        for(int i = 0; s[i]; i++){
            if(char_map.count(s[i])){
                start = max(start, char_map[s[i]] + 1);  // 在子串中重复出现了，更新子串的起点
            }
            char_map[s[i]] = i;
            max_len = max(max_len, i - start + 1);
        }
        return max_len;
    }
};

```

使用usedChar存放出现过的字符，key是那个字符，value是字符对应的索引。

`start <= usedChar[s[i]]`
这行代码的作用是把在start之前的在usedChar中的字符排除在外。

我们以‘tmmzuxta’为例。当遇到第二个t时，start在第二个m的下标。如果不加这个判断，start会从t之后重新开始，最大长度是4。但是我们的正确答案是6。


```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_len = 0, 0
        mapping = {}    # mapping char to it's index
        for i, char in enumerate(s):
            if char in mapping:
                # char is occured before, update start
                start = max(start, mapping[char] + 1)
            mapping[char] = i
            max_len = max(max_len, i - start + 1)
        return max_len
```