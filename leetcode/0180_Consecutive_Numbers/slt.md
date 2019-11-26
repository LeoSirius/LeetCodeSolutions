### 思路1 使用case和自联结

```sql
SELECT DISTINCT Num as ConsecutiveNums
FROM (
    SELECT Num, 
        CASE
            WHEN @prev = Num THEN @count := @count + 1
            WHEN (@prev := Num) IS NOT NULL THEN @count := 1
        END AS CNT
    FROM Logs, (SELECT @prev := NULL, @count := NULL) AS t
) AS temp
WHERE temp.CNT >= 3;
```