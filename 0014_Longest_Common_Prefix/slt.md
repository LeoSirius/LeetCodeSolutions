## 思路1 对每一列，遍历所有字符串，比较那一列的字符

## 思路2 利用zip打包，set去重

利用zip可以将字符串数组中的单个字符串中的每个字符依次打包。然后再用set去重，就可以知道答案了

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        return min(strs)
```