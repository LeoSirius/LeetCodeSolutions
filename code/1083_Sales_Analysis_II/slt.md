### 思路1

利用子查询，找出买了iphone的buyer，再用not in即可。

注意WHERE和GROUP BY的先后顺序

```sql
SELECT s.buyer_id
FROM Sales s JOIN Product p
ON s.product_id=p.product_id
WHERE p.product_name="S8" AND s.buyer_id NOT IN
(
SELECT s.buyer_id
FROM Sales s JOIN Product p
ON s.product_id=p.product_id
WHERE p.product_name="iPhone")
GROUP BY s.buyer_id;
```
