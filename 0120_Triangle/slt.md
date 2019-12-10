### 思路1 bottom-up dp

树状结构很容易让人想到DFS，但是这道题兄弟节点向下都会有一个share branch，如果用DFS，会有很多overlapping subproblems。

换个思路，假设x和y是k的子节点，如果x和y的path值都确定了，那么k的path值就是path(k) += min(path(x), path(y))。所以这道题用DP才是最佳方案。

DP也有两个思路，一是top-down，而是bottom-up

top-down的方案我们还需要n^2的空间来存储中间数据，而bottom-up的方案我们用原有数组来存放。

总结一下，这道题bottom-up的dp是时间和空间都相对较优的方法。
