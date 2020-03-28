### 思路1

```sql
FROM Activity a1 INNER JOIN Activity a2
ON a1.player_id=a2.player_id AND a1.event_date >= a2.event_dat
```

这样得到的结果是a1表的时间是大于等于a2表的

如2016-03-01>=2016-03-01，结果是1个2016-05-02 >= 2016-05-02和2016-03-01，结果是两个，以此类推。这样正好实现了累加。

```sql
SELECT a1.player_id, a1.event_date, sum(a2.games_played) AS games_played_so_far
FROM Activity a1 INNER JOIN Activity a2
ON a1.player_id=a2.player_id AND a1.event_date >= a2.event_date
GROUP BY a1.player_id, a1.event_date;
```
