### Solution1 前缀和 + 暴力

- 时间复杂度 O(n^2)
- 空间复杂度 O(n)

若 a == b, 则有 a ^ b == 0, 

a = prexor[i-1] ^ prexor[j-1]
b = prexor[j-1] ^ prexor[k]

即 prexor[i-1] ^ prexor[j-1] ^ prexor[j-1] ^ prexor[k] == 0
即 prexor[i-1] ^ prexor[k] == 0
即 prexor[i-1] == prexor[k]

即这个等式成立时，中间所有j的取值都满足
