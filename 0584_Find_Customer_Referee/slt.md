### 思路1

注意好对NULL的处理即可。

```sql
SELECT name
FROM customer
WHERE referee_id != 2 OR referee_id IS NULL;
```
