### 思路1 dp

注意，状态方程dp[i][j]表示的是边长，不是面积。

对于最左边一列和最上面一行，dp都是0。

When i > 0 and j > 0, if matrix[i][j] = '0', then dp[i][j] = 0 since no square will be able to contain the '0' at that cell. If matrix[i][j] = '1', we will have dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1, which means that the square will be limited by its left, upper and upper-left neighbors.

if matrix[i][j] == '0':
    dp[i][j] = 0
else:
    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1


是min因为只有左、上、左上三个方向都能组成square，[i][j]才能组成square

另外注意c++的min只能接收两个参数。

```cpp
for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
        if (!i || !j || matrix[i][j] == '0') {
            dp[i][j] = matrix[i][j] - '0';
        } else {
            dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1;
        }
        sz = max(dp[i][j], sz);
    }
}
```

上面的空间是O(mn)，类似之前的一些dp。我们也可以优化空间到O(n)

```cpp
vector<int> pre(n, 0), cur(n, 0);
for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
        if (!i || !j || matrix[i][j] == '0') {
            cur[j] = matrix[i][j] - '0';
        } else {
            cur[j] = min(pre[j - 1], min(pre[j], cur[j - 1])) + 1;
        }
        sz = max(cur[j], sz);
    }
    fill(pre.begin(), pre.end(), 0);
    swap(pre, cur);
}
```
