### 思路1 brute-force

题目是叫我们实现这个函数，而不是调用这个函数。
直接以每个haystack字符作为起点，依次匹配needle中的字符。注意对成立条件的判断，这样大大缩短运行时间。

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.size(), n = needle.size();

        // i的上界是等于m-n的，如m=10， n=3，i最后等于7，最后还剩两个格子，加上i本身正好是3
        // 如  aaaab和ab, 5 - 2 = 3，但i要循环4次
        for(int i = 0; i <= (m - n); ++i){
            int j = 0;
            for(; j < n; ++j){
                if(haystack[i+j] != needle[j]){
                    break;
                }
            }
            if(j == n){
                return i;
            }
        }
        return -1;
    }
};
```

python利用切片可以写得很简洁

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1 
```