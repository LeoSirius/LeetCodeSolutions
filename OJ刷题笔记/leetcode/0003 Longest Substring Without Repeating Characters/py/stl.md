## 思路1 用一个dict存放出现过的character

使用usedChar存放出现过的字符，key是那个字符，value是字符对应的索引。

`start <= usedChar[s[i]]`
这行代码的作用是把在start之前的在usedChar中的字符排除在外。

我们以‘tmmzuxta’为例。当遇到第二个t时，start在第二个m的下标。如果不加这个判断，start会从t之后重新开始，最大长度是4。但是我们的正确答案是6。