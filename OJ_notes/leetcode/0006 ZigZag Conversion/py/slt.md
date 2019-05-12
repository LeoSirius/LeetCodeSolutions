## 思路1 利用字符串list进行转换

我们新建一个`list`来存放字符串，这个list的字符串个数就是`numofRows`。遍历原字符串，不断的将遍历到的字符加载每一行的后面，遇到`boundary`则改变`step`的方向。这里的`boundary`就是0和`numofRows-1`。