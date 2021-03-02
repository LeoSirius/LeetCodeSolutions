### 思路1 利用hash的思想

> Time complexity: O(N)
> Space complexity: O(N)

由于最后要返回的是索引的数组。用hash的key来存放数组中一个元素的值，而用hash的value来存放那个值得索引。这样就建立了数组元素值对数组元素索引的映射。

这个算法的性能取决于hash find的时间复杂度。本身外层循环是O(N)
cpp  unordered_map find()的时间复杂是常量。所以最终的时间复杂度还是O(N)

返回vector的顺序不重要。

