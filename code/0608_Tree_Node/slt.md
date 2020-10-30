### 思路1 left join + case when

```sql
SELECT t1.id,
CASE
  WHEN t1.p_id IS NULL THEN "Root"
  WHEN t2.p_id IS NULL THEN "Leaf"
  ELSE "Inner"
END AS Type
FROM tree t1 LEFT JOIN tree t2
ON t1.id=t2.p_id
GROUP BY t1.id;
```
