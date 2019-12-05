### 思路1

```sql
FROM Activity a1 INNER JOIN Activity a2
ON a1.player_id=a2.player_id AND a1.event_date >= a2.event_dat
```

这两联结后，数据变成：

1 2016-03-01 1 2016-03-01  5

1 2016-05-02 1 2016-03-01  5
1 2016-05-02 1 2016-05-02  6

1 2017-06-25 1 2016-03-01  5
1 2017-06-25 1 2016-05-02  6
1 2017-06-25 1 2017-06-25  1

最后一列是a2的games_played。最后再用group和求和就行了

```sql
SELECT a1.player_id, a1.event_date, sum(a2.games_played) AS games_played_so_far
FROM Activity a1 INNER JOIN Activity a2
ON a1.player_id=a2.player_id AND a1.event_date >= a2.event_date
GROUP BY a1.player_id, a1.event_date;
```
