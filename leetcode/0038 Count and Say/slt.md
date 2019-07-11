### 思路1 直接暴力计算

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        s = ['1']
        result = '1'

        # if n == 1, will return '1'
        for i in range(n-1):
            start = 0
            temp = []

            while start < len(s):
                count = 1           # count表示s[start]的个数
                next = start + 1

                while next < len(s) and s[start] == s[next]:
                    next += 1
                    count += 1      # 数出s[start]的个数，并让start跳到后面一个不同的元素
                
                temp.append(str(count))
                temp.append(s[start])
                start = next
            result = ''.join(temp)
            s = temp
        return result
```