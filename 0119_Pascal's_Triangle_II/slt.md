### Solution 1

The result we need is only one line. So there is no need to store all lines of triangle, just one line will satisfy.

We iterate from back to front to avoid res[j-1] be overridden.

SpaceCompexity: O(rowIndex)

### Solution 1.1

类似1，但不用从后往前，也可以只用一行 tmp array
