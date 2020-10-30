### 思路1

双重循环遍历s和words，用两个hash，一个记录words中的word count，另一记录s中出现了的word count。

时间复杂度`O(s.size() * words.size())`