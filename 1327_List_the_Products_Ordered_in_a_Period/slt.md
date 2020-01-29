### 思路1

```sql
SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p JOIN Orders o
ON p.product_id=o.product_id
WHERE MONTH(o.order_date)=2
GROUP BY p.product_id
HAVING SUM(o.unit) >= 100;
```
