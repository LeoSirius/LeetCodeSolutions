### 思路1 

这道题同1076，也有个多个答案的问题

用ALL
用子查询求出最大的价格是多少，再用>=

```sql
SELECT seller_id
FROM Sales
GROUP BY seller_id
HAVING SUM(price) >= ALL(
    SELECT SUM(price) FROM Sales GROUP BY seller_id
);
```
