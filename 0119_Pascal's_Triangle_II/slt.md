### Solution 1

The result we need is only one line. So there is no need to store all lines of triangle, just one line will satisfy.

We iterate from back to front to avoid res[j-1] be overridden.
