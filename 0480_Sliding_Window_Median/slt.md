### 思路1 双堆 - 双堆对顶

https://leetcode-cn.com/problems/sliding-window-median/solution/python-shuang-dui-shuang-ha-xi-dui-liang-jb34/

- 设中位数为X
- 小于X的数放在最大堆中，大于X的数放在最小堆中


由于一开始是把所有元素都放在最小堆中，然后k//2下取整把另一半元素放在最大堆中的

- 如果k是奇数，则每次取最小堆的元素为答案
- 如果k是偶数，则取两个堆的对顶，把平均值放入答案

