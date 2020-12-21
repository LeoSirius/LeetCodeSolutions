### 思路1

注意两点，一是求加权平均值，二是日期范围

```sql
SELECT p.product_id, ROUND(SUM(p.price * u.units) / SUM(u.units), 2) AS average_price
FROM Prices p JOIN UnitsSold u
ON p.product_id=u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
```
