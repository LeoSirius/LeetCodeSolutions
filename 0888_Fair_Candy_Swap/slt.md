### 思路1 hash

假设alice交换x，bob交换y，则有公式：

sumA - x + y = sumB + x - y

化简得：

x = y + (sumA - sumB) / 2

因此只需要遍历每个Bob中的y，判断对应的x是否在alice中即可。

