### 思路1 dp 三指针法

所有的ugly number：

(1) 1×2, 2×2, 3×2, 4×2, 5×2, …  所有正整数 * 2
(2) 1×3, 2×3, 3×3, 4×3, 5×3, …  所有正整数 * 3
(3) 1×5, 2×5, 3×5, 4×5, 5×5, …  所有正整数 * 5
We can find that every subsequence is the 
ugly-sequence itself (1, 2, 3, 4, 5, …) multiply 2, 3, 5.

我们只要用三个指针，把这些数按照大小顺序排列起来就行了。
