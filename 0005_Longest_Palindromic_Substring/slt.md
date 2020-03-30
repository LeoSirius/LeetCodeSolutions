## 思路1 dp

dp(i, j) represents whether s(i ... j) can form a palindromic substring, dp(i, j) is true when s(i) equals to s(j) and s(i+1 ... j-1) is a palindromic substring. When we found a palindrome, check if it's the longest one. Time complexity O(n^2).

`dp[l][r]`代表`s[l,r]`是否是回文。
如果`s[l] == s[r]`且`s[l+1, r-1]`是回文，则`s[l,r]`是回文。

如果`s[l] == s[r]`且`r-l<=2`，则`s[l,r]`是回文。如aba或aa。

## 思路2 中心散开法

时间复杂度O(n^2)。下面的python实现的方法如果改成c++的话，会比cpp现在用的方法慢。因为spread_out被调用了两次。

