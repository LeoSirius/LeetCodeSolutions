### 思路1 DFS

我们用l和r分别表示还需要加到字符串中的数目。为了保证字符串合法，剩下的右括号必须大于等于左括号，如果剩下的右括号小于左括号，说明有左括号没有与之匹配的右括号。


```python
class Solution:
    def generateParenthesis(self, n: int):
        if not n:
            return []
        l, r, res = n, n, []       # l, r分别表示剩下的左右括号的数目
        self.dfs(l, r, res, '')
        return res

    def dfs(self, l, r, res, string):
        if r < l:
            return
        # 左右括号都用完
        if not l and not r:
            res.append(string)
            return
        if l:
            self.dfs(l-1, r, res, string+'(')
        if r:
            self.dfs(l, r-1, res, string+')')
```

另一种check字符串合法的方式是让l一开始为n，r一开始为0。l减1，r则要加1，因为加了一个左括号，就需要一个右括号与之匹配。

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if(n == 0)
            return res;
        dfs(n, 0, res, "");
        return res;
    }

    void dfs(int l, int r, vector<string> &res, string str){
        if(l == 0 && r == 0){
            res.push_back(str);
            return;
        }
        if(l > 0) dfs(l-1, r+1, res, str+"(");
        if(r > 0) dfs(l, r-1, res, str+")");
    }
};
```