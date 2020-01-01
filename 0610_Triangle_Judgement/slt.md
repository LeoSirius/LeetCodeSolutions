### 思路1

用CASE...WHEN...

```sql
SELECT x, y, z,
    (CASE WHEN x + y > z AND x + z > y AND y + z > x THEN "Yes"
    ELSE "No" END) AS "triangle"
FROM triangle;
```
