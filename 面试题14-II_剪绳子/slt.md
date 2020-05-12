### 思路1

这道题由于要取余，不能像上一题用dp max的方法
贪心算法，取3，具体见。

https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/

贪心法则：尽可能分解出多的 3, 3的个数为a，余数为b，b可能的值是0,1,2

b = 0, return 3^a
b = 1, 将末尾的3+1看成4，返回3^(a-1) + 2 * 2
b = 2, 返回3^a * 2