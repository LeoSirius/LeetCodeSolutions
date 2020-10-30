### 思路1

For each tower, its surface area is 4 * v + 2
However, 2 adjacent tower will hide the area of connected part.
The hidden part is min(v1, v2) and we need just minus this area * 2

Time Complexity:
O(N^2)
