### Solution1 数学方法

时间复杂度 O(n)
空间复杂度 O(1)

高斯求和法求得 _sum = (n * (n+1)) / 2

再遍历 nums，用 _sum 依次减去每一个数，留下来的就是结果
