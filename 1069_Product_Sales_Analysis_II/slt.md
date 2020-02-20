### 思路1

```sql
SELECT s.product_id, SUM(s.quantity) AS total_quantity
FROM Sales s JOIN Product p
ON s.product_id=p.product_id
GROUP BY s.product_id;
```
