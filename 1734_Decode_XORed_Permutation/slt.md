### Solution1 数学模拟

首先复习异或运算运算法则

- a ^ a = 0
- a ^ 0 = a
- a ^ b = b ^ a
- a ^ b = c  <->  c ^ b = a

如果这道题有「首位元素」或者「结尾元素」，则便和 1720 一样了

首先 encoded 中的每一项如下

[perm[0] ^ perm[1], perm[1] ^ perm[2], ..., perm[n-2] ^ perm[n-1]

例如：

01 12 23 34  （n = 5，encoded 偶数个）

得

0123

则把 encoded 中每隔一项进行异或，得：

res1 = perm[0] ^ perm[1] ^ perm[2] ^ perm[3] ^ ... ^ perm[n-2]

第二部 利用交换律

res2 = perm[0] ^ perm[1] ^ ... ^ perm[n-1]

则 res2 = res1 ^ perm[n-1]
推出：perm[n-1] = res1 ^ res2 这样便转化成了 1720