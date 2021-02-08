### 思路1 dp

dp[i]表示以i结尾的最长连续子数组的长度

本题需要两个状态方程

- up[i]表示以i结尾，并且`arr[i-1] < arr[i]`的最长湍流子数组的长度
- down[i]表示以i结尾，并且`arr[i-1] > arr[i]`的最长湍流子数组的长度

状态转移方程：

- up[i] = down[i-1] + 1, if arr[i-1] < arr[i]
- down[i] = up[i+1] + 1, if arr[i-1] > arr[i]

如果`arr[i-1] == arr[i]`则两个状态都回归1
