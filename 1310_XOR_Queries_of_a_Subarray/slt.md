### Solution1 前缀和

时间复杂度 O(n + m)
空间复杂度 O(n)

复习异或的运算性质

- a ^ 0 = a
- a ^ b ^ b = a
- a ^ b = b ^ a

因此异或也和加法一样，[i, j] = pre[j] ^ pre[i]
