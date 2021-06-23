### Solution1 数学方法

假设最少操作次数是 k，k 次操作后所有数都相等。设相等的数为 target
对 n - 1 个元素操作 k 次，则一共增加了 k * (n-1)

则有

target * n = sum(nums) + k * (n-1)

而 target = min(nums) + k

这样便可以解出 k

k = sum - min(nums) * n
