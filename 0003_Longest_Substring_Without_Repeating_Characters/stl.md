## 思路1 HashMap存放字符到索引的映射

如果用传统的双重循环遍历每个子串的话，时间复杂度是O(n^2)。我们这里使用map的时间复杂度只有O(n^logn)。（假定map search的时间复杂度为O(n^logn)，比如c++中）

map的key为s中的字符，value为字符的索引

start标记最近一个没有重复的字符的索引。如果当前字符已经在map中，则和start进行比较，start取最靠后的，这样保持start记录的是最近一个没有重复字符的开始索引。
另外，map和set两种容器的底层结构都是红黑树，所以容器中不会出现相同的元素，因此count()的结果只能为0和1。

注意start只能向前移动`start = max(start, char_map[s[i]] + 1);`。


如  axxxxbxxbxxxxa

如果start没有去max的话，遇到最后一个a时，start又跳回去了。把两个b都包括进去了
