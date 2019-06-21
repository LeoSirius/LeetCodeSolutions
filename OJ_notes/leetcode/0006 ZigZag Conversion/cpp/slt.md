## 思路1 同python


```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows <= 1)
            return s;
        const int len = int(s.size());
        string *strs = new string[numRows];  // array of string, size = numRows
        int row = 0, step = 1;
        for(int i = 0; i < len; i++){
            strs[row].push_back(s[i]);
            if(row == 0){
                step = 1;
            }else if(row == numRows - 1){
                step = -1;
            }
            row += step;
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