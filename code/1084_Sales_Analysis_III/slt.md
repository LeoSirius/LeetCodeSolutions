### 思路1 用子查询

注意这道题的含义，仅在春天出售的商品。如果一个商品还在其他时间内出售，则不在这道题的结果里。

```sql
SELECT product_id, product_name
FROM Product
WHERE product_id NOT IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date < "2019-01-01" OR sale_date > "2019-03-31"
);
```
