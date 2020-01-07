### 思路1

用子查询你找出所有单个元素，再在其中用max找出最大的。不能再GROUP的select语句中直接用max，因为这个max同count一样，则是组内的。

```sql
SELECT MAX(num) as num
FROM (
    SELECT num
    FROM my_numbers
    GROUP BY num
    HAVING COUNT(num)=1
) AS t;
```