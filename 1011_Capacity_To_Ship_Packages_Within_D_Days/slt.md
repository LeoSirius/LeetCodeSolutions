### Solution1

在不考虑天数的情况下，最低运力是 max(weights)，最高运力是 sum(weights)

然后在 [max(weights), sum(weights)] 之间用二分 + 试探的方法找到满足D天的最小运力
