### 思路1 使用max

注意这道题对NULL的处理。

```sql
SELECT IFNULL(
(SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1,1)
, NULL) AS SecondHighestSalary;
```
