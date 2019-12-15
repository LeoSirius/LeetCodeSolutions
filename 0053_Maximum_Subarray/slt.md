### 思路1 dp

`maxSubArray(int A[], int i)`表示包含了A[i]统计的最大子列和。

`maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i];`
