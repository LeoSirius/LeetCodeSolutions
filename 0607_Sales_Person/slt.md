### 思路1

先用内联结筛选出销售给RED的所有orders中包含的sales_id，再用NOT IN

```sql
SELECT s.name
FROM salesperson s
WHERE s.sales_id NOT IN (
    SELECT o.sales_id
    FROM orders o INNER JOIN company c
    ON o.com_id=c.com_id WHERE c.name="RED");
```
