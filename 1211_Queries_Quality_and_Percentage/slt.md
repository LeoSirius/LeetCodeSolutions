### 思路1

```sql
SELECT query_name,
ROUND(AVG(rating/position), 2) AS quality,
ROUND((SUM(if(rating<3, 1, 0)) / count(*)) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
```
