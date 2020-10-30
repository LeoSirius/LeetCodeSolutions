### 思路1

min和group by一起使用。如果不加min，GROUP BY会显示分组内的第一条数据。

```sql
SELECT player_id, min(event_date) as first_login
FROM Activity
GROUP BY player_id;
```
