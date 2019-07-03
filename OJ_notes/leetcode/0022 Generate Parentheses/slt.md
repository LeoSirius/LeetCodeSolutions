## 思路1 DFS

剩下的右括号必须大于等于左括号，如果剩下的右括号小于左括号，说明有左括号没有与之匹配的右括号。


```python
class Solution:
    def generateParenthesis(self, n: int):
        if not n:
            return []
        l, r, res = n, n, []
        self.dfs(l, r, res, '')
        return res

    def dfs(self, l, r, res, string):
        if r < l:
            return
        # 左右括号都用完
        if not l and not r:
            print('res.append string = ' + string)
            res.append(string)
            return
        if l:
            self.dfs(l-1, r, res, string+'(')
        if r:
            self.dfs(l, r-1, res, string+')')
```