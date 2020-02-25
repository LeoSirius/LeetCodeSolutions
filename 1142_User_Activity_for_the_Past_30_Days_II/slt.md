### 思路1 使用distinct直接计算

`总session数 / 总用户数`

```sql
SELECT
IFNULL(
    ROUND(COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id), 2), 
0)
AS average_sessions_per_user
FROM Activity
WHERE DATEDIFF('2019-07-27', activity_date) < 30;
```
