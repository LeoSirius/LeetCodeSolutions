### 思路1

1 选出每个user_id第一次登陆的时间

```sql
SELECT user_id, MIN(activity_date) AS login_date
FROM Traffic
WHERE activity='login'
GROUP BY user_id;
```

2 再用90天筛选，并用你group by求数量

```sql
SELECT login_date, COUNT(*) AS user_count
FROM (
    SELECT user_id, MIN(activity_date) AS login_date
    FROM Traffic
    WHERE activity='login'
    GROUP BY user_id
) AS t
WHERE DATEDIFF("2019-06-30", login_date)<=90
GROUP BY login_date;
```
