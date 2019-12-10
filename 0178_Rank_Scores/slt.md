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
