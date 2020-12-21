### 思路1

左右子树都不存在 return 1
只有一个:  左右子树有一个不存在，则 min_depth = 1 + l + r; 这时lr中必有一个是0，而当前节点不是叶结点
都有:     左右子树都存在，则min_depth = min(left, right) + 1
