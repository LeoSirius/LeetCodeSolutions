### Solution1 位运算 + Trie

- 时间复杂度 O(n * logc)
    n 是 nums 的长度，c 是字典树集合的大小，这里是 2
- 空间复杂度 O(n * logc)
    n 中的每一个数在字典树中都要用 logc 的空间

遍历一遍 nums，利用字典树的特性找到 当前 nums[i] 与前面所有 [nums[0], nums[i-1]] 异或的最大值
