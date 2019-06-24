## 思路1 利用字符串list进行转换

我们创建一个字符串数组来存放结果，这个数组的长度就是`numofRows`。遍历原字符串，不断的将遍历到的字符加载每一行的后面，遇到`boundary`则改变`step`的方向。这里的`boundary`就是0和`numofRows-1`。

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        const int len = int(s.size());

        if(numRows <= 1 || numRows >= len)
            return s;

        string *strs = new string[numRows];  // array of string, size = numRows
        int index = 0, step = 1;
        for(int i = 0; i < len; i++){
            strs[index].push_back(s[i]);
            if(index == 0){
                step = 1;
            }else if(index == numRows - 1){
                step = -1;
            }
            index += step;
        }
        s.clear();
        for(int i = 0; i < numRows; i++){
            s.append(strs[i]);
        }
        delete [] strs;
        return s;
    }
};
```

在python中我们直接用`''.join(list_name)`的形式把`list`转换为字符串

```py
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s
        step = 1
        index = 0
        res = [''] * numRows
        for i, v in enumerate(s):
            # cur_line is not index
            res[index] += v
            if index == numRows-1:
                step = -1
            elif index == 0:
                step = 1
            index += step
        return ''.join(res)
```