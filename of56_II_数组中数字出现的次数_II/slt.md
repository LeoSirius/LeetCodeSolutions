### 思路1 位运算统计

x ^ 0 = 0
x ^ 1 = ~x

考虑数字的二进制形式，对于出现三次的数字，各 二进制位 出现的次数都是 3 的倍数。
因此，统计所有数字的各二进制位中 1 的出现次数，并对 3 求余，结果则为只出现一次的数字。

用two和one分别表示三种状态的两位：00, 01, 10

00 -> 01 -> 10 -> 00 -> ...

假设新的一个数的位是n（=1或=0）

计算one

if two == 0:
  if n == 0:
    one = 0
  if n == 1:
    one = ~one  (从00到01，或从01到10)

if two == 1:   # 这时不管n是0还是1，one都还是1
  one = 0

用异或简化第一种情况

if two == 0:
  one = one ^ n
if two == 1:   # 这时不管n是0还是1，one都还是1
  one = 0

再用于位运算，继续简化

one = one ^ n & ~two


计算two

可以看出和计算one是一样的

如果one=1，

则当前情况只能是01，

- 如果n是0，则还是01
- 如果n是1，则变成10

如果one=0

则当前10或00

10 + 1 = 11 % 3 = 00
00 + 1 = 01

00 + 0 = 00
10 + 0 = 10

if one == 1:
  two = 0
if one == 0:
  if n == 0:
    two = 0
  if n == 1:
    two = ~two

有
two = two ^ n & ~one


另一个理解方法：

为了区分出现一次的数字和出现三次的数字，使用两个位掩码：seen_once 和 seen_twice。
位掩码 seen_once 仅保留出现一次的数字，不保留出现三次的数字。

# first appearance: 
# add num to seen_once 
# don't add to seen_twice because of presence in seen_once

# second appearance: 
# remove num from seen_once 
# add num to seen_twice

# third appearance: 
# don't add to seen_once because of presence in seen_twice
# remove num from seen_twice


seen_once = seen_twice = 0


如x = 2,   10

first:

seen_once = ~seen_twice & (seen_once ^ num) = ~(00) & (00 ^ 10) = 11 & 10 = 10
seen_twice = ~seen_once & (seen_twice ^ num) = ~(10) & (00 ^ 10) = 01 & 10 = 00

second:

seen_once = ~seen_twice & (seen_once ^ num) = ~(00) & (10 ^ 10) = 11 & 00 = 00
seen_twice = ~seen_once & (seen_twice ^ num) = ~(00) & (00 ^ 10) = 11 & 10 = 10

third:

seen_once = ~seen_twice & (seen_once ^ num) = ~(10) & (00 ^ 10) = 01 & 10 = 00
seen_twice = ~seen_once & (seen_twice ^ num) = ~(00) & (10 ^ 10) = 11 & 00 = 00



### 思路2 统计个位1出现的个数，再模3

思路同一，但是计算方法用常规的方法来统计

