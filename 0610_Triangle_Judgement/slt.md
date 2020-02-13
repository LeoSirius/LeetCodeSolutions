### 思路1

用CASE...WHEN...

```sql
SELECT x, y, z,
IF((x+y>z AND x+z>y AND y+z>x), 'Yes', 'No') AS triangle
FROM triangle;
```
