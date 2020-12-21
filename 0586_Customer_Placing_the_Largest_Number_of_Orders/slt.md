### 思路1

GROUP BY + COUNT + LIMIT

用了group by之后的count，count的是分组内的数据的个数。不管count是出现在group by前还是后。

```sql
SELECT customer_number
FROM orders 
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
```