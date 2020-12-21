### 思路1

group by 然后

每组的产品种类数量 = 总产品种类数量

```sql
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key)=(SELECT COUNT(*) FROM Product);
```
