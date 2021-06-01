### Solution1 模拟 + 前缀和

对于每个 query 三元组，计算能最早和最晚吃到 query[0] 类糖的时间，再判断 query[1] 是否在这个时间内

问题转换为求吃 query[0] 类糖果的最早和最晚时间

- fav类型：t = query[0]        
- fav天数：d = query[1] + 1    题目的天从 0 算，我们从 1 算
- 每天吃糖上限：c = query[2]

另外预先求得 candiesCount 的前缀和数组 presum，以便快速求得 t 类糖果之前有多少糖果。

我们的 presume 数组从 1 开始

求最早时间（第一颗 t 糖的最小时间）（以最大速率 c 吃糖）：

`(presum[t] / c) + 1`

最晚时间（最后一个 t 糖的最晚时间）（以最小速率 1 吃糖）：

`persum[t+1]`






