class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return ''
        l, r, res = n, n, []
        self.dfs(l, r, res, '')
        return res
        

    def dfs(self, l, r, res, string):
        if r < l:
            return
        if not l and not n:
            res.append(string)
            return
        if l:
            self.dfs(l-1, r, res, string+'(')
        if r:
            self.dfs(l, r-1, res, string+')')