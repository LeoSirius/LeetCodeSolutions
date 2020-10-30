### 思路1 递归

```cpp
class Solution {
public:
    string countAndSay(int n) {
        if(n == 1) return "1";
        if(n == 2) return "11";
        string last_say = countAndSay(n-1);
        string new_say = "";
        int count = 1;
        for(int i = 1; i < last_say.size(); i++){
            if(last_say[i] != last_say[i-1]){
                new_say.push_back('0'+count);
                new_say.push_back(last_say[i-1]);
                count = 1;
            }else{
                count++;
            }
            if(i == last_say.size() - 1){
                new_say.push_back('0'+count);
                new_say.push_back(last_say[i]);
            }
        }
        return new_say;
    }
};
```

### 思路x 直接暴力计算

利用python中list的特性，可以很好的直接计算。

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        say_list = ['1']
        # if n == 1, will return '1', so the for loop is  n-1 times
        for i in range(n-1):
            start = 0
            tmp = []
            while start < len(say_list):
                count = 1               # count表示s[start]的个数
                next = start + 1
                while next < len(say_list) and say_list[start] == say_list[next]:
                    next += 1
                    count += 1          # 数出s[start]的个数，并让start跳到后面一个不同的元素
                tmp.append(str(count))
                tmp.append(say_list[start])
                start = next
            say_list = tmp
        return ''.join(say_list)
```
