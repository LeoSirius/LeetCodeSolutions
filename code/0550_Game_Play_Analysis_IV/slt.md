### 思路1

总体思路：用子查询分别求出  “第一天登录后的一天登录过的玩家的数量” 和 “总玩家数量”

先求所有玩家第一天登录的日期

```sql
SELECT player_id, MIN(event_date) FROM Activity GROUP BY player_id;
```

在用这个日期和DATEDIFF，求出第一天登录后的一天登录过的玩家的数量

```sql
SELECT COUNT(DISTINCT a.player_id)
FROM Activity a JOIN 
(SELECT player_id, MIN(event_date) AS event_date FROM Activity GROUP BY player_id) b
ON a.player_id=b.player_id AND DATEDIFF(a.event_date, b.event_date)=1;
```


总玩家数量

```sql
SELECT COUNT(DISTINCT player_id)
FROM Activity;
```

最后ROUND来除就行

```sql
SELECT ROUND(
(SELECT COUNT(DISTINCT a.player_id)
FROM Activity a JOIN 
(SELECT player_id, MIN(event_date) AS event_date FROM Activity GROUP BY player_id) b
ON a.player_id=b.player_id AND DATEDIFF(a.event_date, b.event_date)=1
) / 
(
SELECT COUNT(DISTINCT player_id)
FROM Activity), 2
) AS fraction;
```

