### 思路1 使用WHERE子句

```sql
SELECT Score, (
    SELECT COUNT(DISTINCT Score)
    FROM Scores
    WHERE Score >= s.Score) AS Rank
FROM Scores s
ORDER BY Score DESC;
```

对于外部SELECT的每一条score，我们再用内部的SELECT，统计scores表中有多少个比外部记录大的记录的个数。

### 思路2 JOIN

```sql
SELECT s1.Score, COUNT(DISTINCT(s2.Score)) AS Rank
FROM Scores s1 JOIN Scores s2
WHERE s1.score<=s2.score
GROUP BY s1.Id
ORDER BY Rank;
```

理论上联表查询的效率会优于子查询，但是这里两者都是取笛卡尔积。实际跑出来子查询的速度快很多
