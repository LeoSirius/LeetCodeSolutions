### 思路1 hash

利用一个map和set

map保存pattern字符到单词的映射，
set保存已经加入到map中的单词，防止不用pattern对应的word重复
