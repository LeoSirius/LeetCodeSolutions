### 思路1 使用UNION ALL

```sql
SELECT t.id, COUNT(t.id) AS num
FROM (
    SELECT requester_id AS id
    FROM request_accepted
UNION ALL
    SELECT accepter_id AS id
    FROM request_accepted
) t
GROUP BY t.id
ORDER BY COUNT(t.id) DESC LIMIT 1;
```

注意UNION会去掉重复的值，UNION ALL会保留重复的值
