## 思路1 对每一列，遍历所有字符串，比较那一列的字符

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        // p 表示列号。对每一列，遍历所有字符串
        for(int p = 0; strs.size()>0; prefix += strs[0][p++]){
            for(int i = 0; i < strs.size(); ++i){
                // p已经走到了最短那个字符串的尽头 or
                // p列有字符不同， 则返回
                if(p >= strs[i].size() || (i > 0 && strs[i][p] != strs[i-1][p]))
                    return prefix;
            }
        }
        return prefix;
    }
};
```

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