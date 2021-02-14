### Solution1 Greedy

```
Time complexity: O(N^2)
Space cpmplexity: O(1)
```

https://leetcode-cn.com/problems/couples-holding-hands/solution/tan-xin-suan-fa-shi-qing-lu-qian-shou-bi-eeel/

Traverse every even index, find the value's couple, then swap.

Find x's couple skill:

- x is even, x ends with 0 in bianry, x ^ 1 turns 0 to 1, get x + 1
- x is odd, x ends with 1 in binary, x ^ 1 turns 1 to 0, get x - 1

