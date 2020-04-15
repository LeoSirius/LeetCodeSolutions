### 思路1 利用子查询

注意相同product_id和year的record可能有多个。如果直接用GROUP BY + MIN 则只会选出一个。

```sql
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
    SELECT product_id, MIN(year) AS year FROM Sales GROUP BY product_id
);
```
