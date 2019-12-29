### 思路1

用左联结。注意处理NULL不能用=，NULL=NULL是false。NULL 和任何值比较都是false

判断是不是NULL必须用 `is null` or `is not null`

```sql
SELECT e.name, b.bonus
FROM Employee e LEFT JOIN Bonus b
ON e.empId=b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```
