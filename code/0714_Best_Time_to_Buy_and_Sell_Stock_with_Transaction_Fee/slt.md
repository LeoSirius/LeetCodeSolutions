### 思路1 dp

has[i]表示第i天手上有股票，not[i]表示第i天手上没有股票，递归方程：

- has[i] = max(has[i-1], not[i-1] - prices[i])       （第二项表示在第i天买入股票）
- not[i] = max(not[i-1], has[i-1] + prices[i] - fee)  （第二项表示在第i天将股票卖出，需扣除手续费）



