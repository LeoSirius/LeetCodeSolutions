### 思路1

这道题要找出follower的follower数量

先联结两表，这样f2的followee是f1中的follower，

```sql
SELECT *
FROM follow f1 JOIN follow f2
ON f1.follower=f2.followee;
```

然后再找出f2的followee有多少follower就可以了。

```sql
SELECT f1.follower, COUNT(DISTINCT f2.follower) AS num
FROM follow f1 JOIN follow f2
ON f1.follower=f2.followee
GROUP BY f2.followee;
```
