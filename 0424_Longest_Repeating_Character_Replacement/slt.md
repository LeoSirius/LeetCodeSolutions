### 思路1 sliding window

每次for loop都r++，如果

用history_char_max记录当前窗口内出现的最多的相同的字符的个数。
如果 history_char_max + k > 窗口长度，则窗口是满足要求的。否则 l += 1
