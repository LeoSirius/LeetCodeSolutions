### 思路1

利用上一题（511）的结果作为子查询

```sql
SELECT a.player_id, a.device_id
FROM Activity a
WHERE (a.player_id, a.event_date) IN (
    SELECT player_id, min(event_date)
    FROM Activity
    GROUP BY player_id
);
```
