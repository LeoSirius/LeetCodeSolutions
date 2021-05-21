### 思路1 brute-force

- 时间复杂度 O(m * n)
- 空间复杂度 O(1)

题目是叫我们实现这个函数，而不是调用这个函数。
直接以每个haystack字符作为起点，依次匹配needle中的字符。

python利用切片可以写得很简洁

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1 
```

### 思路2 暴力破解 -- 双指针

用一次遍历 + 回溯

直接用双重循环的话会超时

### 思路3 KMP
