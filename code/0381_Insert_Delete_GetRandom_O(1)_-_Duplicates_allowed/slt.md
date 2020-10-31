### 思路1

用一个数组nums来保存所有insert的元素

- insert时把元素加到nums尾部，时间复杂度O(1)
- getRandom时，按nums的长度取一个随机索引返回，时间复杂度O(1)

另外用一个hash表维护数在nums的索引

- key：nums中的数
- val：是一个集合，由key数在nums中的索引组成

删除时，设删除x，

1. 从hash表的集合中取一个x的索引i。并从集合中remove i
2. 把nums[i]和nums[nums.length-1]（设nums[nums.length-1] 是 y）交换
3. 最后再更新原来y的索引集合
4. 最后再把换到nums最后的x pop掉

以上所有操作的时间复杂度都是O(1)，加起来也是O(1)
