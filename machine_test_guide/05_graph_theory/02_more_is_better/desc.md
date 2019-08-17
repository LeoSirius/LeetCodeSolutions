### 题目描述

Mr Wang wants some boys to help him with a project. Because the porject is rather complex, the more boys come, the better it will be. Of course there are certain requirements. Mr Wang selected a room big enough to hold the boys. The boy who are not been chosen has to leave the room immediately. There are 10,000,000 boys in the room numbered from 1 to 10,000,000 at the very beginning. After Mr Wang's selection any two of them who are still in this room should be firends(direct or indirect), or there is only one boy left. Given all the direct firend-pairs, you should decide the best way.

### 输入

The first lien of the input contains an integer n (0 <= n <= 100,000) - the number of direct friend-pairs. The following n lines each contains a pair of numbers A and B separated by a single space that sugests A and B are direct friends. （A != B, 1 <= A, B <= 10,000,000）

### 输出

The output in one line contains exactly one integer equals to the maximum number of boys Mr Wang may keep.

### 样例输入

```
4
1 2
3 4
5 6
1 6
4
1 2
3 4
5 6
7 8
```

### 样例输出

```
4
2
```