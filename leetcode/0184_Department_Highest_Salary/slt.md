### 思路1 

大体上分成两部，一是内联结两个表。二是内联结的两个条件，一个自然是department的id，另一个是用GROUP BY和max求得的每个部门最大的Salary。

```sql
SELECT 
    d.Name AS Department, 
    e.Name AS Employee,
    e.Salary
FROM
    Employee e INNER JOIN Department d
ON
    e.DepartmentId=d.id
    AND
    (e.Salary, e.DepartmentId) IN
        (SELECT max(Salary), DepartmentId
        FROM Employee GROUP BY DepartmentId);
```
