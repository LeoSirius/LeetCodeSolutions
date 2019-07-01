## 思路1 利用双重循环

```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if(digits.size() == 0)
            return res;
        string charmap[10] = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        res.push_back("");
        for(int i = 0; i < digits.size(); ++i){
            vector<string> tmp_res;
            string chars = charmap[digits[i]-'0'];

            // 遍历当前数字对应的字符串
            for(int c = 0; c < chars.size(); ++c){
                // 对于已经在res中的每个字符串，每个都再加上刚才遍历的字符
                for(int j = 0; j < res.size(); ++j){
                    tmp_res.push_back(res[j]+chars[c]);
                }
            }
            res = tmp_res;
        }
        return res;
    }
};
```

python可以利用列表生成式。除此之外，还可以用递归。

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [x + y for x in prev for y in additional]
```