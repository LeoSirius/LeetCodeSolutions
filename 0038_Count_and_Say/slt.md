### 思路1 递归模拟


### 思路x 直接暴力计算

利用python中list的特性，可以很好的直接计算。

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        say_list = ['1']
        # if n == 1, will return '1', so the for loop is  n-1 times
        for i in range(n-1):
            start = 0
            tmp = []
            while start < len(say_list):
                count = 1               # count表示s[start]的个数
                next = start + 1
                while next < len(say_list) and say_list[start] == say_list[next]:
                    next += 1
                    count += 1          # 数出s[start]的个数，并让start跳到后面一个不同的元素
                tmp.append(str(count))
                tmp.append(say_list[start])
                start = next
            say_list = tmp
        return ''.join(say_list)
```
