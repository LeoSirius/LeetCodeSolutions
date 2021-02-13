### Solution1 hash - operate on original array, mapping number to index

1. Add size to every element of nums[nums[i]] for i in range(size)
This will make every number(appeared in array)'s corresponding index > size

2. Traverse array, find value <= size. Then the index is the answer element.

